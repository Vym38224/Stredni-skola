from os.path import basename, splitext
import re
import random
import tkinter as tk
from tkinter import *

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Matematika"

    def __init__(self):

        super().__init__(className=self.name)
        self.lbl = tk.Label(self, text="Matematika")
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl.grid(row=0)
        self.lblVl = tk.Label(self, text="")
        self.lblVl.grid(row=3, column=2)
        self.generuj()
        self.entry = Entry(self, width=5)
        self.entry.grid(row=2, column=3)
        self.bind('<Return>', self.kontrola)
        self.btn = tk.Button(self, text="Konec", command=self.quit)
        self.btn.grid(row=3, column=3)
       


    def kontrola(self, event):
        try:
            if int(self.entry.get()) == self.vysledek:
                self.lblVl.config(text="SPRÁVNĚ", fg="green")

            else:
                self.lblVl.config(text="ŠPATNĚ",fg="red")

            self.generuj()
            self.entry.delete(0, END)
        except ValueError:
            return

    def generuj(self):
        self.funkce = random.choice([self.plus, self.deleno, self.minus, self.krat])
        self.priklad = self.funkce()
        self.lbl.config(text=self.priklad)
        self.lbl.grid(row=2, column=2)

    def plus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100 - self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        self.znamenko = "+"
        return f"{self.cisloA}{self.znamenko}{self.cisloB} ="

    def deleno(self):
        self.cisloA = random.randint(1, 10)
        self.vysledek = random.randint(1, 10)
        self.cisloB = self.cisloA * self.vysledek
        self.znamenko = "/"
        return f"{self.cisloB}{self.znamenko}{self.cisloA} ="

    def minus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, self.cisloA)
        self.vysledek = self.cisloA - self.cisloB
        self.znamenko = "-"
        return f"{self.cisloA}{self.znamenko}{self.cisloB} ="

    def krat(self):
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10)
        self.vysledek = self.cisloA * self.cisloB
        self.znamenko = "*"
        return f"{self.cisloA}{self.znamenko}{self.cisloB} ="

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop() 