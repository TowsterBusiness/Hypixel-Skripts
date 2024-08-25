import sys
from pynput.keyboard import Listener, Key, KeyCode
from time import sleep
from pyautogui import *
import threading
import random

pressed_keys = []

running = True

mouse_pressed = False

def key_logger():
    def on_press(key):
        if key == KeyCode.from_char("a"):
            print("Stopping...")
            keyUp('space')
            keyUp('s')
            keyUp('a')
            keyUp('w')
            keyUp('d')
            sys.exit()
        
            
        
    
    with Listener(on_press=on_press) as listener:
        listener.join()
        
        

def macro():
    wait_time = 0.4
    while(True):
      keyDown('d')
      sleep(wait_time)
      keyUp('d')
      keyDown('shift')
      sleep(wait_time)
      keyUp('shift')
      keyDown('a')
      sleep(wait_time)
      keyUp('a')
      keyDown('shift')
      sleep(wait_time)
      keyUp('shift')
        
        
th1 = threading.Thread(target=key_logger)
th2 = threading.Thread(target=macro)        
        
def main():
    sleep(2)
    th1.start()
    th2.daemon = True
    th2.start()
    

if __name__ == "__main__":
    main()
