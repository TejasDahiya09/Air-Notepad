# Air Notepad – Hand Gesture Controlled Drawing App ✋🖊️

Air Notepad is a virtual drawing canvas that works entirely through **hand gestures** using **MediaPipe** + **OpenCV**.  
No keyboard. No mouse. Just your hands.

This project is fully interactive and supports **tool switching**, **color selection**, and **drawing in the air**.

---

## 🚀 Features

### ✨ Hand Gesture Features
- **Right Hand** → Draw on canvas using the index finger  
- **Left Hand Pinch** → Select tools and colors from the menu  
- **Pinch = Click** gesture  
- Smooth drawing with stabilization  

### 🧰 Tools
- Pen  
- Brush  
- Eraser  

### 🎨 Color Palette
- Red, Blue, Green, Yellow, Purple, White, Orange, Pink  

### 🧹 Canvas Actions
- Clear entire canvas  
- Realtime preview overlay  

---

## 📁 Project Structure

```
airnotepad/
│
├── main.py            # Main application loop
├── gestures.py        # Hand detection + pinch detection
├── menu.py            # Tool panel UI + button detection
├── tools.py           # Tools, colors, global selected states
├── drawing.py         # Smoothing + drawing logic
└── config.py          # Settings (canvas size, smooth factor, etc.)
```

---

## 🛠️ Installation

### 1. Clone the repository
```
git clone https://github.com/your-username/airnotepad.git
cd airnotepad
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the application
```
python main.py
```

---

## 🧩 Requirements

- Python 3.8+
- A webcam
- Mediapipe
- OpenCV
- NumPy

(All installed via `requirements.txt`)

---

## 🎮 Controls

### **Left Hand**
| Gesture | Action |
|--------|---------|
| Pinch (thumb + index) | Select tool/color/clear |

### **Right Hand**
| Gesture | Action |
|--------|---------|
| Index finger extended | Draw |
| No index finger | Stop drawing |

---

## 🏁 Quit
Press **Q** to exit the application.

---

## 📸 Demo
Add screenshots or GIFs here once recorded.

---

## 📜 License
This project is free to use and modify.

