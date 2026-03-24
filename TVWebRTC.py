import asyncio
import websockets
import json
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

WS_PORT = 8765
HTTP_PORT = 8766

sender = None
receivers = set()

# ── WebSocket Signaling ────────────────────────────────
async def handler(ws):
    global sender

    print("Client connected")

    try:
        async for message in ws:
            data = json.loads(message)

            # 🔹 Register roles
            if data.get("role") == "sender":
                sender = ws
                print("✅ Sender registered")

            elif data.get("role") == "receiver":
                receivers.add(ws)
                print(f"📺 Receiver registered: {len(receivers)}")

            # 🔹 Offer → all receivers
            elif data.get("type") == "offer":
                for r in receivers:
                    await r.send(message)

            # 🔹 Answer → sender
            elif data.get("type") == "answer":
                if sender:
                    await sender.send(message)

            # 🔹 ICE exchange
            elif data.get("type") == "ice":
                if ws == sender:
                    for r in receivers:
                        await r.send(message)
                else:
                    if sender:
                        await sender.send(message)

    except Exception as e:
        print("Error:", e)

    finally:
        if ws == sender:
            sender = None
            print("❌ Sender disconnected")

        if ws in receivers:
            receivers.remove(ws)
            print(f"❌ Receiver disconnected: {len(receivers)}")


# ── HTTP Server ────────────────────────────────────────
def start_http():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    server = HTTPServer(("0.0.0.0", HTTP_PORT), QuietHandler)

    print(f"\n🌐 Open these URLs:")
    print(f"👉 Sender:   http://<your-ip>:{HTTP_PORT}/sender.html")
    print(f"👉 Receiver: http://<your-ip>:{HTTP_PORT}/receiver.html\n")

    server.serve_forever()


# ── Main ───────────────────────────────────────────────
async def main():
    print(f"🚀 WebRTC Signaling Server: ws://0.0.0.0:{WS_PORT}")

    threading.Thread(target=start_http, daemon=True).start()

    async with websockets.serve(handler, "0.0.0.0", WS_PORT):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())