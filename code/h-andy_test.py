from pynput import keyboard 
from pynput.keyboard import Key
import threading

def on_release(key):
    try:
        print(str(key))
        if key.char in {'1', '2', '3', '4'}:
            print(f"Number key {key.char} was released – do something")
    except AttributeError:
        # Handle special keys like Shift, Ctrl, etc.
        if key == Key.up:
            print("Hello world!")

should_disconnect = False

def start_keyboard_listener():
    listener = keyboard.Listener(on_release=on_release)
    listener.start()  # Non-blocking
    print('Keyboard listener has been started')
    return listener

# Start keyboard listener in a separate thread so that it does not block the main program 
listener_thread = threading.Thread(target=start_keyboard_listener)
listener_thread.daemon = True
listener_thread.start()

while not should_disconnect:
    pass
