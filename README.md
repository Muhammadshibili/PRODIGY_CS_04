# ⌨️ Cross-Platform Keylogger Project

**For Educational Purposes and Cybersecurity Research Only**

---

## 📝 Overview

This project demonstrates two distinct methods of keystroke logging, highlighting the architectural differences between Windows and Linux (Wayland) security models.

While standard keyloggers rely on high-level API hooking, this project provides insight into how modern Linux environments using **Wayland** restrict input capture.

---

## 🚀 Features

- **Linux Version:** Uses the `evdev` library to interface directly with kernel input devices.
- **Windows Version:** Uses the `pynput` library to utilize Win32 API hooks.
- **Raw Data Capture:** Records special keys such as Backspace, Shift, Ctrl, etc.

---

## 🛠️ Installation & Usage

## 🐧 Option 1: Linux (Kali / Ubuntu)

### Requirements

The Linux script may require root privileges to read input devices:

```bash
sudo apt update
sudo apt install python3-evdev
````

### Run the Script

```bash
sudo python3 keylogger_linux.py
```

**Output:** Creates a `keylog.txt` file in the current directory.

---

## 🪟 Option 2: Windows (Windows 10/11)

### Requirements

Install dependency:

```cmd
pip install pynput
```

### Run the Script

```cmd
python keylogger_windows.py
```

---

## ⚠️ Ethical Disclaimer

This project is strictly for educational and authorized cybersecurity research purposes only.

**DO NOT use this for malicious activity.**



