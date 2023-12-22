import os
import tkinter as tk
from tkinter import Tk, Label, Button, filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x300")

        mixer.init()  # Initialize the mixer module from pygame

        self.current_song = None

        # GUI components
        self.label = Label(root, text="Created by Nikhil", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.btn_select = Button(root, text="Select Song", command=self.select_song)
        self.btn_select.pack(pady=10)

        self.btn_play = Button(root, text="Play", command=self.play_song, state="disabled")
        self.btn_play.pack(pady=10)

        self.btn_stop = Button(root, text="Stop", command=self.stop_song, state="disabled")
        self.btn_stop.pack(pady=10)

        self.volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume", command=self.set_volume)
        self.volume_scale.set(50)
        self.volume_scale.pack(pady=10)

    def select_song(self):
        file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

        if file_path:
            self.current_song = file_path
            self.label.config(text=os.path.basename(file_path))
            self.btn_play.config(state="normal")
            self.btn_stop.config(state="normal")

    def play_song(self):
        if self.current_song:
            mixer.music.load(self.current_song)
            mixer.music.play()

    def stop_song(self):
        mixer.music.stop()

    def set_volume(self, value):
        volume = int(value) / 100
        mixer.music.set_volume(volume)    

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()