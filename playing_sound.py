from tkinter import *
from pydub import AudioSegment
from pygame import mixer

window = Tk()
window.title("MP3 Player")
window.geometry("500x900")

def play():
    src = "Azana_-_Your_Love.mp3"
    dst = "test.wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    mixer.init()
    mixer.music.load('test.wav')
    mixer.music.play()

def pause():
    mixer.music.pause()
    

play_button = Button(window,text="Play Button", command=play)
pause_button = Button(window,text="Pause Button", command=pause)
unpause_button = Button(window,text="Unpause Button")
stop_button = Button(window,text="Stop Button")


play_button.grid()
pause_button.grid()
unpause_button.grid()
stop_button.grid()

