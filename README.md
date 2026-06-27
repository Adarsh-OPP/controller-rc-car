# 🎮 Controller RC Car

> **Turn your XInput gamepad into an RC car using its own vibration motors — controlled with WASD.**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square&logo=windows)
![XInput](https://img.shields.io/badge/Controller-XInput-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📺 Demo

[![Watch the Demo](https://img.shields.io/badge/YouTube-Watch%20Demo-red?style=for-the-badge&logo=youtube)](YOUR_YOUTUBE_LINK_HERE)

<!-- Replace YOUR_YOUTUBE_LINK_HERE with your video URL -->
<!-- To show a video thumbnail, upload a thumbnail image to your repo and use this: -->
<!-- [![Demo Video](your-thumbnail.png)](YOUR_YOUTUBE_LINK_HERE) -->

---

## ✨ What is this?

Inspired by the viral Steam Controller trick — this script fires your gamepad's **left and right rumble motors** at different intensities to physically move it across a flat surface, just like an RC car.

Place your controller **face-down** on a smooth table and drive it with your keyboard.

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `W` | Forward |
| `A` | Turn Left |
| `D` | Turn Right |
| `ESC` | Quit |

---

## ⚙️ Compatible Controllers

Works with **any XInput controller** on Windows, including:

- ✅ Xbox 360 Controller
- ✅ Xbox One / Series Controller
- ✅ Ant Esports or any other 3rd party controller with dual motors and XInput
- ✅ Any generic XInput gamepad

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Adarsh-OPP/controller-rc-car.git
cd controller-rc-car
```

### 2. Install dependency

```bash
pip install keyboard
```

### 3. Run as Administrator

> ⚠️ **Must be run as Administrator** — the `keyboard` library requires elevated permissions on Windows.

```bash
python controller_rc.py
```

---

## 🔧 Configuration

Open `controller_rc.py` and edit the two lines at the top:

```python
CONTROLLER = 0       # 0, 1, 2, or 3 — if multiple controllers are connected
MOTOR_POWER = 1.0    # Motor strength: 0.0 (off) to 1.0 (full power)
```

---

## 💡 Tips for Best Movement

- 🪵 **Smooth surfaces work best** — wood, tile, or glass table
- 📱 Carpet will kill the movement — stick to hard floors
- 🔋 Make sure your controller is **fully charged or plugged in**
- 🎮 If direction feels reversed, swap `"a"` and `"d"` values in `MOVE_MAP`

---

## 🛠️ How It Works

Your gamepad has two independent rumble motors:

- **Left motor** — strong, low-frequency
- **Right motor** — weak, high-frequency

By running only one at a time, the controller spins in that direction. Running both makes it push forward. The script uses Windows' built-in **XInput API** via `ctypes` — no extra drivers needed.

---

## 📦 Requirements

- Windows 10 / 11
- Python 3.7+
- `keyboard` library (`pip install keyboard`)
- Any XInput-compatible gamepad

---

## 📄 License

MIT License — free to use, modify, and share.

---

<p align="center">Made with ❤️ by <a href="https://github.com/Adarsh-OPP">Adarsh-OPP</a></p>
