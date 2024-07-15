from os.path import basename, splitext
import tkinter as tk
from tkinter import *


# from tkinter import ttk


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárna"

    def __init__(self):
        super().__init__(className=self.name)
        v1 = tk.IntVar(self)
        v2 = tk.IntVar(self)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna", borderwidth=14)
        self.lbl.pack()
        #Transakce
        self.variable = tk.IntVar(self)
        self.lbl1 = tk.Label(self, text="Transakce:")
        self.lbl1.pack(anchor=W)
        self.radiobutton1 = Radiobutton(self, text="Nákup", variable=self.variable, value=1).pack(anchor=W)
        self.radiobutton2 = Radiobutton(self, text="Prodej", variable=self.variable, value=2).pack(anchor=W)
        self.variable.set(1)
        #kurzovní lístek
        self.lbl2 = tk.Label(self, text="Kurzovní lístek:")
        self.lbl2.pack(anchor=W)
        self.listbox = tk.Listbox(self)
        self.listbox.pack(anchor=W)
        self.listbox.bind("<ButtonRelease-1>", self.kliknu)       
        f = open("smenarna/listek.txt", "r")
        slovnik = {}
        for line in f:
            self.listbox.insert(tk.END,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])
        #Kurz
        self.lbl3 = tk.Label(self, text="Kurz:")
        self.lbl3.pack(anchor=W)
        self.price = tk.StringVar()
        self.amount = tk.IntVar()
        self.amountLbl= tk.Label(self, textvariable= self.amount) 
        self.amountLbl.pack()
        self.pricel= tk.Label(self, textvariable= self.price) 
        self.pricel.pack()
        #Výpočet
        self.lbl2 = tk.Label(self, text="Výpočet:")
        self.lbl2.pack(anchor=W)
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.btn2 = tk.Button(self, text="Výpočet", command=self.vypocet)
        self.btn2.pack()
        self.vysledek = tk.IntVar()
        self.vysledekl= tk.Label(self, textvariable= self.vysledek)
        self.vysledekl.pack()
        #Quit
        self.bind("<Escape>", self.quit)
        self.btn1 = tk.Button(self, text="Quit", command=self.quit)
        self.btn1.pack()

    
    def vypocet(self,event=None):  
        a = int(self.entry.get())
        b = int(self.amount.get())
        c = float(self.price.get().replace(",","."))
        self.vysledekVar = float(a*c/b)
        self.vysledek.set(self.vysledekVar)

    
    def kliknu(self, event):
        index = self.listbox.curselection()[0]
        f = open("smenarna/listek.txt")
        self.lines = f.readlines()
        self.amountVar = self.lines[index].split()[1]
        self.amount.set(self.amountVar)
        if self.variable.get() == 1: 
            self.priceVar = self.lines[index].split()[3] 
        else:
            self.priceVar = self.lines[index].split()[2] 
        self.price.set(self.priceVar)
       
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()