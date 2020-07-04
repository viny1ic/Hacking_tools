from pynput import keyboard

def run_on_press(key):
    print(str(key))

def exit_condition(key):
    if key=='Key.esc':
        return False

with keyboard.Listener(on_press=run_on_press, on_release=exit_condition) as listener:
    listener.join()