from tkinter import *
from ttkbootstrap.constants import *

import ttkbootstrap as tb 

root = tb.Window(themename="superhero")
root.title("Lista de Tarefas!")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

# Style
my_style = tb.Style()
my_style.configure("success.Outline.TButton", font=("Poppins", 18))

# Button
my_button = tb.Button(
    text="Clique Aqui!",
    style="success.Outline.TButton",
    bootstyle="success",
    width=20)
my_button.pack(pady=20)


root.mainloop()