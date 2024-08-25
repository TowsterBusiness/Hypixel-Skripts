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
    keyDown('space')
    while(True):
        for i in range(5):
            keyDown('s')
            sleep(47.8 + (random.random() * 0.2))
            keyDown('d')
            keyUp('s')
            sleep(47.8 + (random.random() * 0.3))
            keyUp('d')
        sleep(0.2)  
        keyDown('w')
        keyDown('a')
        sleep(2.9)
        keyUp('w')
        keyUp('a')
        
        
th1 = threading.Thread(target=key_logger)
th2 = threading.Thread(target=macro)        
        
def main():
    sleep(2)
    th1.start()
    th2.daemon = True
    th2.start()
    

if __name__ == "__main__":
    main()
