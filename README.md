# 📺 LocalCast WebRTC – Real-Time Screen Sharing (LAN)

A lightweight, browser-based **screen casting system** built using **WebRTC + WebSockets**.

Stream your Mac/PC screen to a TV (or any browser) over the same WiFi network with **low latency (~100–300ms)** — no external services required.

---

## 🚀 Features

* ⚡ Real-time screen sharing using **WebRTC**
* 📡 Peer-to-peer streaming (no heavy backend streaming)
* 🌐 Works entirely on **local network (LAN)**
* 📺 Supports **multiple receivers (TVs)**
* 🔌 Simple Python signaling server
* 🧠 Optimized for low latency (resolution + FPS control)

---

## 🏗️ Architecture

```
Sender (Browser)
   ↓  (WebRTC)
Python Signaling Server (WebSocket)
   ↓
Receiver (TV Browser)
```

* The server **does NOT stream video**
* It only handles **signaling (offer/answer/ICE)**
* Video flows **directly between devices (P2P)**

---

## 📁 Project Structure

```
.
├── server.py        # WebRTC signaling + HTTP server
├── sender.html      # Screen sharing client (Mac/PC)
└── receiver.html    # TV display client
```

---

## ⚙️ Requirements

* Python 3.8+
* Install dependency:

```bash
pip install websockets
```

* Modern browser (Chrome recommended)

---

## ▶️ How to Run

### 1️⃣ Start Server

```bash
python server.py
```

You’ll see:

```
Sender:   http://<your-ip>:8766/sender.html
Receiver: http://<your-ip>:8766/receiver.html
```

---

### 2️⃣ Open Sender (Laptop / Mac)

Open in browser:

```
http://<your-ip>:8766/sender.html
```

Click:

👉 **Start Sharing**
👉 Select screen/window

---

### 3️⃣ Open Receiver (TV / Second Device)

Open:

```
http://<your-ip>:8766/receiver.html
```

---

## 🎯 Expected Result

* Receiver opens → black screen
* Start sharing → ⚡ instant live stream appears

---

## ⚡ Performance Tuning

The system is optimized using:

* Resolution limit: **1280x720**
* Frame rate: **15 FPS**
* WebRTC P2P streaming

### Recommended tweaks:

```js
frameRate: { max: 10–15 }
width: { max: 1280 }
height: { max: 720 }
```

---

## ⚠️ Limitations

* 📡 Works best on **same WiFi network**
* 📺 Some **Smart TV browsers may be slow**
* 🔁 Multiple receivers increase load on sender
* 🔊 Audio streaming not included (yet)

---

## 🧪 Troubleshooting

### ❌ No video on TV

* Open receiver **before** sender
* Ensure same network
* Check browser console logs

---

### ❌ Lag / Slow performance

* Reduce resolution / FPS
* Test on laptop/mobile (TV may be bottleneck)

---

### ❌ Connection not established

* Check firewall / ports (8765, 8766)
* Ensure WebSocket connection is successful

---

## 🚀 Future Improvements

* 🔥 Multi-TV optimized streaming (SFU)
* 🔐 Pairing system (like Chromecast)
* 🔊 Audio support
* 📱 Mobile sender support
* 🌍 Internet-based streaming (TURN server)

---

## 🤝 Contributing

Feel free to fork, improve, and submit PRs!

---

## 📜 License

MIT License

---

## 💡 Inspiration

Built as a lightweight alternative to:

* Chromecast
* AirPlay
* Screen sharing tools

---

## 🙌 Author

Built with ❤️ for fast, simple, real-time casting
