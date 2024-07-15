import math
import tkinter as tk

from tkinter import *
from os.path import basename, splitext


dva_operandy = {}
dva_operandy["+"] = lambda a, b: a + b
dva_operandy["-"] = lambda a, b: a - b
dva_operandy["*"] = lambda a, b: a * b
dva_operandy["/"] = lambda a, b: a / b
dva_operandy["//"] = lambda a, b: a // b
dva_operandy["**"] = lambda a, b: a ** b

jeden_operand = {}
jeden_operand["sin"] = math.sin
jeden_operand["cos"] = math.cos
jeden_operand["tan"] = math.tan



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "kalkulacka"

    def __init__(self):
        super().__init__(className=self.name)
        self.expression = ""
        self.zasobnik = []
        self.equation = StringVar()
        self.geometry("416x377")
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Kalkulačka", fg="dark blue")
        self.lbl.grid(row = 1,column=4)
        self.btn = tk.Button(self, text = "Konec",bg="pink", command = self.quit, height=1, width=7)
        self.btn.grid(row = 5, column = 6)
        self.btnz = tk.Button(self, text="Zapsat",bg="green", command=self.fce, height=1, width=7)
        self.btnz.grid(row=4, column=6)
        self.btn1 = Button(self, text=' 1 ', command=lambda: self.press(1), height=1, width=7)
        self.btn1.grid(row = 2, column = 1)
        self.btn2 = Button(self, text=' 2 ', command=lambda: self.press(2), height=1, width=7)
        self.btn2.grid(row= 2, column=2)
        self.btn3 = Button(self, text=' 3 ', command=lambda: self.press(3), height=1, width=7)
        self.btn3.grid(row= 2, column=3)
        self.btn4 = Button(self, text=' 4 ', command=lambda: self.press(4), height=1, width=7)
        self.btn4.grid(row=3, column=1)
        self.btn5 = Button(self, text=' 5 ', command=lambda: self.press(5), height=1, width=7)
        self.btn5.grid(row=3, column=2)
        self.btn6 = Button(self, text=' 6 ', command=lambda: self.press(6), height=1, width=7)
        self.btn6.grid(row=3, column=3)
        self.btn7 = Button(self, text=' 7 ', command=lambda: self.press(7), height=1, width=7)
        self.btn7.grid(row=4, column=1)
        self.btn8 = Button(self, text=' 8 ', command=lambda: self.press(8), height=1, width=7)
        self.btn8.grid(row=4, column=2)
        self.btn9 = Button(self, text=' 9 ', command=lambda: self.press(9), height=1, width=7)
        self.btn9.grid(row=4, column=3)
        self.btn0 = Button(self, text=' 0 ', command=lambda: self.press(0), height=1, width=7)
        self.btn0.grid(row=5, column=1)
        self.plus = Button(self, text=' + ', command=lambda: self.press("+"), height=1, width=7)
        self.plus.grid(row=2, column=4)
        self.minus = Button(self, text=' - ', command=lambda: self.press("-"), height=1, width=7)
        self.minus.grid(row=3, column=4)
        self.multiply = Button(self, text=' * ', command=lambda: self.press("*"), height=1, width=7)
        self.multiply.grid(row=4, column=4)
        self.divide = Button(self, text=' / ', command=lambda: self.press("/"), height=1, width=7)
        self.divide.grid(row=5, column=4)
        self.radical = Button(self, text=' //', command=lambda: self.press("//"), height=1, width=7)
        self.radical.grid(row=5, column=5)
        self.power = Button(self, text=' **', command=lambda: self.press("**"), height=1, width=7)
        self.power.grid(row=4, column=5)
        self.decimal = Button(self, text='.', command=lambda: self.press("."), height=1, width=7)
        self.decimal.grid(row=5, column=2)
        self.clearr = Button(self, text='C', command=self.clear, height=1, width=7)
        self.clearr.grid(row=5, column=3)
        self.sin = Button(self, text='sin', command=lambda: self.press("sin"), height=1, width=7)
        self.sin.grid(row=2, column=5)
        self.cos = Button(self, text='cos', command=lambda: self.press("cos"), height=1, width=7)
        self.cos.grid(row=3, column=5)
        self.tan = Button(self, text='tan', command=lambda: self.press("tan"), height=1, width=7)
        self.tan.grid(row=2, column=6)
        self.pi = Button(self, text='π', command=lambda: self.press(3.141592653589793), height=1, width=7)
        self.pi.grid(row=3, column=6)
        self.btnup = Button(self, text = "↑", command=self.up, height=1, width=7 )
        self.btnup.grid(row = 10, column = 7)
        self.btndown = Button(self, text = "↓", command=self.down, height=1, width=7)
        self.btndown.grid(row = 11, column = 7)
       
        
        self.frame = Frame(self)
        self.frame.grid(row = 11, column = 7)

        self.entry = Entry(self, textvariable=self.equation, width=40)
        self.entry.grid(rowspan = 10, columnspan = 7)
        
        self.listbox = tk.Listbox(self, width=40)
        self.listbox.grid(rowspan = 11, columnspan = 7)

    def press(self, num):   
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
    
        except:
            self.equation.set(" error ")
            self.expression = ""

    def clear(self):
        self.listbox.delete(0,tk.END)
        self.expression = ""
        self.equation.set("")

    def fce(self):
        self.zpracuj(self.entry.get())
        self.expression = ""
        self.equation.set("")
    
    def listbox_reload(self):
        self.listbox.delete(0, END)
        for item in self.zasobnik:
            self.listbox.insert(END, item)

    def up(self, event = None):
        if self.listbox.get(ACTIVE) != "":
            item = self.listbox.curselection()[0]
            self.zasobnik[item], self.zasobnik[item - 1] = self.zasobnik[item - 1], self.zasobnik[item]
            self.listbox_reload()
          
            self.listbox.selection_set(item - 1)
            self.listbox.activate(item - 1)
        else:
            pass

    def down(self, event = None):
        if self.listbox.get(ACTIVE) != "":
            item = self.listbox.curselection()[0]
            self.zasobnik[item], self.zasobnik[item + 1] = self.zasobnik[item + 1], self.zasobnik[item]
            self.listbox_reload()
          
            self.listbox.selection_set(item + 1)
            self.listbox.activate(item + 1)          
        else:
            pass
        
    def quit(self, event = None):
        super().quit()


    def operace(self, token, event=None):
            token = str(self.entry.get())
            if token.upper() == "Q":
                exit()
            if token.upper() == "PI":
                self.zasobnik.append(math.pi)
            if token.upper() == "SW":
                a =  self.listbox.get(tk.END)
                b =  self.listbox.get(tk.END-1)
                self.zasobnik.append(b)
                self.zasobnik.append(a)
            if token in dva_operandy.keys():
                if len(self.zasobnik) >= 2:
                    b = self.zasobnik.pop()
                    a = self.zasobnik.pop()
                    self.zasobnik.append(dva_operandy[token](a, b))
                else:
                    print("Nemám dostatek operadnů!")
            if token in jeden_operand.keys():
                if len(self.zasobnik) >= 1:
                    a = self.zasobnik.pop()
                    self.zasobnik.append(jeden_operand[token](a))
                else:
                    print("Nemám dostatek operadnů!")
            self.listbox.delete(0,tk.END)
            for token in self.zasobnik:
                self.listbox.insert(tk.END,token)


    def zpracuj(self, token, event=None):
        try:
            self.zasobnik.append(float(token))
            self.listbox.insert(tk.END,token)
        except ValueError:
            self.operace(self,token)


app = Application()
app.mainloop()


