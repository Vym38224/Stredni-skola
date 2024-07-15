import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

from pylab import linspace, pi, plot,sin,cos, show,grid,legend
from os.path import basename, splitext
from tkinter import *
from scipy.io import wavfile
from pydub import AudioSegment
from pydub.playback import play

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Generování průběhu"

    def __init__(self):
        super().__init__(className=self.name)
        self.var_entryF = tk.IntVar()
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl1 = tk.Label(self, text="", font=7)
        self.lbl1.pack()  
        self.lblF = tk.Label(self, text=u"Frekvence:")
        self.lblF.pack(anchor=W)
        self.entryF  = tk.Entry(self, textvariable = self.var_entryF, width = 15, justify=CENTER)
        self.entryF.pack()
        self.btn3 = tk.Button(self, text="Načíst graf", command=self.graf)
        self.btn3.pack()
        self.btn3 = tk.Button(self, text="Play", command=self.play)
        self.btn3.pack()
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.pack()

    def graf(self):
        self.frekvence = self.var_entryF.get()
        self.sample_rate = 44100
              
        self.t = np.arange(0, 3, 2/self.sample_rate)
        self.x = (2*pi*self.frekvence*self.t )
        self.signal = np.sin(self.x)

        def norm(data):
            min_v = min(data)
            max_v = max(data)
            return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1

        self.noise = 1*np.random.randn(*self.signal.shape)
        self.dirty =  norm(self.signal + self.noise)

        plt.plot(self.t,self.signal)
        plt.title("Signál")
        plt.xlabel("Time [s]")
        plt.ylabel("U V]")
        plt.grid()
        plt.show()

        self.signal *= 32767
        self.signal = np.int16(self.signal)
        wavfile.write("sound.wav", self.sample_rate,self.signal)       
        
    def play(self):
        #pass
        self.song = AudioSegment.from_wav("sound.wav")
        play(self.song)

    def quit(self, event=None):
        super().quit()
        
app = Application()
app.mainloop()
