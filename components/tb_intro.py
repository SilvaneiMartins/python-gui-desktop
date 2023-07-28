from tkinter import *
from ttkbootstrap.constants import *

import ttkbootstrap as tb 

root = tb.Window(themename="superhero")
root.title("Lista de Tarefas!")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

# Cria uma função
counter = 0
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="Silvanei Martins!")
    else:
        my_label.config(text="Sam Developer!")

# Cria uma label
my_label = tb.Label(
        text="Silvanei Martins", 
        font=("Poppins", 28), 
        bootstyle="danger, inverse")
my_label.pack(pady=50)

# Cria um botão
my_button = tb.Button(
    text="Clique Aqui!", 
    bootstyle="success, outline",
    command=changer)
my_button.pack(pady=20)

root.mainloop()




