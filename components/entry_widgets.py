from tkinter import *
from ttkbootstrap.constants import *

import ttkbootstrap as tb 

root = tb.Window(themename="superhero")
root.title("Lista de Tarefas!")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

# Cria uma função de entrada
def speak():
    my_label.config(text=f"Sua mensagem: {my_entry.get()}", font=("JetBrains Mono", 18))
    my_entry.delete(0, END)

# Cria uma ferramenta de entrada
my_entry = tb.Entry(
    root,
    bootstyle="primary",
    font=("JetBrains Mono", 18),
    width=5,
    foreground="gray",
    show="*")
my_entry.pack(pady=50)

# Cria um botão
my_button = tb.Button(
    root,
    text="Clique Aqui!",
    bootstyle="danger outline",
    command=speak)
my_button.pack(pady=20)

# Cria um texto
my_label = tb.Label(root, text="")
my_label.pack(pady=20)


root.mainloop()