# Hand-Tracking-and-video-controller

Control your **Windows system** using just your **hand gestures**!  
Built using **Python**, **MediaPipe**, and **OpenCV**, this project lets you interact with your PC touch-free.

---

## ✅ Features

| Gesture                              | Action                    |
|--------------------------------------|---------------------------|
| 👊 Fist                               | Pause media               |
| ✋ Open palm (5 fingers)              | Play media                |
| ✌️ Peace sign (Index + Middle)       | Volume Up                 |
| 🤘 Four fingers (no pinky)           | Volume Down               |
| 👉 Swipe right (2 fingers up)        | Show Desktop (`Win + D`)  |
| 👈 Swipe left (2 fingers up)         | Switch App (`Alt + Tab`)  |

---

## 💻 Requirements

- Windows 10 or 11
- Python 3.7+
- Webcam or phone camera (works with Phone Link or virtual webcam apps)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Justreadingbro/Hand-Tracking-and-video-controller.git
cd hand-gesture-control
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

