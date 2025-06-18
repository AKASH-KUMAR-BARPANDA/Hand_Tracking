# ✋ Real-Time Hand Tracking using MediaPipe & OpenCV

![Hand Tracking Banner](https://user-images.githubusercontent.com/45185276/131640156-c8b17435-0e4c-4038-bf13-d91e94649e8c.gif)

> A real-time hand tracking application using Python, MediaPipe, and OpenCV — implemented in both a modular (OOP) and a script-based format.

---

## 🎯 Aim of the Project

To build a system that can **detect and track human hands in real-time** using webcam input. This can serve as the foundation for gesture recognition, finger counting, hand-based UI controls, sign language detection, and more.

---

## 🔧 Features

- 🧠 **MediaPipe Hands**: Google's powerful hand detection and tracking model.
- 📹 **Real-time Processing**: Works live with your webcam.
- 🎯 **Keypoint Landmark Tracking**: Detects and draws 21 keypoints per hand.
- 🔄 **Modular Version**:
  - Encapsulated in a class for reusability.
  - Separate method for FPS calculation.
- ⚡ **FPS Counter**: Displays real-time frames per second.
- 🔍 **Landmark Highlighting**: Custom point highlighting (e.g., index finger tip `id=12`).

---

## 🗂️ Project Structure

```bash
hand_tracking_project/
│
├── modular_version.py       # ✅ OOP-based version with reusable class
├── simple_script.py         # ⚡ Standalone script version
├── README.md                # 📄 This file
