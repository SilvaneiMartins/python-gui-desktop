from tkinter import *
from ttkbootstrap.constants import *

import ttkbootstrap as tb 

root = tb.Window(themename="superhero")
root.title("Lista de Tarefas!")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

def checker():
    if var1.get() == 1:
        my_label_check.config(text="Você aceitou!")
    else:
        my_label_check.config(text="Você não aceitou!")

my_label_check = tb.Label(text="Termos e Condições", font=("JetBrains Mono", 18))
my_label_check.pack(pady=(40, 10))

# Cria um Checkbox
var1 = IntVar()
my_check = tb.Checkbutton( 
    bootstyle="primary",
    text="Aceito os termos e condições!",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)
my_check.pack(pady=10)

var2 = IntVar()
my_check2 = tb.Checkbutton(
    bootstyle="danger, toolbutton",
    text="Aceito as politicas!",
    variable=var2,
    onvalue=1,
    offvalue=0,
    command=checker)
my_check2.pack(pady=10) 

var3 = IntVar()
my_check3 = tb.Checkbutton(
    bootstyle="warning, toolbutton, outline",
    text="Aceita Termos e Politicas!",
    variable=var3,
    onvalue=1,
    offvalue=0,
    command=checker)
my_check3.pack(pady=10)

var4 = IntVar()
my_check4 = tb.Checkbutton(
    bootstyle="success, round-toggle",
    text="Silvanei Martins!",
    variable=var4,
    onvalue=1,
    offvalue=0,
    command=checker)
my_check4.pack(pady=10)

var5 = IntVar()
my_check5 = tb.Checkbutton(
    bootstyle="secondary, square-toggle",
    text="Sam Developer!",
    variable=var5,
    onvalue=1,
    offvalue=0,
    command=checker)
my_check5.pack(pady=10)

root.mainloop()




