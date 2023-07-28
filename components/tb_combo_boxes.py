from tkinter import *
from ttkbootstrap.constants import *

import ttkbootstrap as tb 

root = tb.Window(themename="superhero")
root.title("Lista de Tarefas!")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

# Cria uma função
def clicker():
    my_label.config(text=f"Voce clicou em {my_combo.get()}!", font=("JetBrains Mono", 18))

def click_bind(e):
    my_label.config(text=f"Voce clicou em {my_combo.get()}!", font=("JetBrains Mono", 18))


# Label
my_label = tb.Label(
    root,
    text="Silvanei Martins",
    font=("Poppins", 18))
my_label.pack(pady=30)

# Cria as opções do combobox
days = [
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
    "Domingo",
]

# Combobox
my_combo = tb.Combobox(
    root,
    bootstyle="success",
    values=days)
my_combo.pack(pady=20)

# Seta o valor padrão
my_combo.current(0)

# Cria um botão
my_button = tb.Button(
    root,
    text="Clique Aqui!",
    bootstyle="success",
    command=clicker)
my_button.pack(pady=20)

# Vincular o combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)


root.mainloop()