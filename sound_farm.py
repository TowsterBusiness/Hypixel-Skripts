import sys
from pynput.keyboard import Listener, Key, KeyCode
from time import sleep
from pyautogui import *
import threading
import random
from pydub import AudioSegment, playback
from pydub.playback import play



        
def macro():
    song = AudioSegment.from_mp3("sound.mp3")
    song2 = AudioSegment.from_mp3("sound2.mp3")
    while(True):
        play(song)
        for i in range(5):
            sleep(48)
            play(song)
            sleep(48)
            play(song)
        sleep(0.2)  
        play(song2)
        sleep(3)
        
th2 = threading.Thread(target=macro)        
        
def main():
    sleep(2)
    th2.start()
    

if __name__ == "__main__":
    main()
    song = AudioSegment.from_mp3("sound.mp3")
    play(song)
