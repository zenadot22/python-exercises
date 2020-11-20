from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#from pydub import AudioSegment
from pygame import mixer

class MusicPlayer:
    def __init__(self, window):
        window.geometry("500x200")
        window.title("Music Player")
        self.load_button = Button(window, text="load", width=10, command=self.load, bg="gold").grid(column=0, row=3)
        self.play_button = Button(window, text="play", width=10, command=self.play, bg="gold").grid(column=1, row=3)
        self.pause_button = Button(window, text="pause", width=10, command=self.pause, bg="gold").grid(column=0, row=4)
        self.stop_button = Button(window, text="stop", width=10, command=self.stop, bg="gold").grid(column=1, row=4)

        self.music_file = False
        self.play_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename() #loading playlist

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
        else:
            messagebox.showinfo(title="Message Box", message='Load song')

    def pause(self):
        if not self.play_state:
            mixer.music.pause()
            self.play_state = True
        else:
            mixer.music.unpause()
            self.play_state = False

    def stop(self):
        mixer.music.stop()

root = Tk()
root.config(bg='black')
app = MusicPlayer(root)
root.mainloop()
