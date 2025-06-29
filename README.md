# 🖐️ Hand-Tracking-and-video-controller

Control your **Windows system** using just your **hand gestures**!  
Built using **Python**, **MediaPipe**, and **OpenCV**, this project lets you interact with your PC touch-free — no keyboard or mouse needed.

---

## ✅ Features

Each gesture is based on a **binary finger code**:  
`[Thumb, Index, Middle, Ring, Pinky] → 0 (down) or 1 (up)`

| Finger Code | Gesture Example         | Action                    |
|-------------|--------------------------|---------------------------|
| `00000`     | 👊 Fist                   | Pause Media               |
| `11111`     | ✋ Open Palm              | Play Media                |
| `01100`     | ✌️ Peace Sign             | Volume Up                 |
| `01111`     | 🤘 Four fingers (no thumb) | Volume Down              |
| `11000`     | 👍 + ☝️ Thumb + Index     | Show Desktop (`Win + D`)  |
| `11100`     | 👉 + middle finger       | Switch App (`Alt + Tab`)  |

---

## 💻 Requirements

- Windows 10 or 11
- Python 3.7+
- Webcam or Phone Camera  
  (Use Phone Link, DroidCam, or OBS Virtual Camera)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Justreadingbro/Hand-Tracking-and-video-controller.git
cd Hand-Tracking-and-video-controller

```
### 2.
```bash
pip install opencv-python mediapipe pyautogui
```
### 3.Make sure your camera is connected. If it shows a black screen, try changing this line:
```bash
cap = cv2.VideoCapture(0)
```
to
```bash
cap = cv2.VideoCapture(1)  # or 2, 3...
```
## 4.  Future Features (To-Do)
### Mouse control via hand movement

### Gesture to text/speech

### Custom gesture training

### App launching by gesture

