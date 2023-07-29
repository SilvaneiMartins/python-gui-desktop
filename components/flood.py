from tkinter import *
from ttkbootstrap.constants import *

import ttkbootstrap as tb 

root = tb.Window(themename="superhero")
root.title("Lista de Tarefas!")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

# Cria uma função de entrada
def starter():
    my_gauge.start()

def stoper():
    my_gauge.stop()

def incrementer():
    my_gauge.step(10)
    my_label.config(text=f"Posição: {my_gauge.variable.get() +10}%")

# Cria uma função de entrada
my_gauge = tb.Floodgauge(
    root,
    bootstyle="success",
    mask="Posição: {}%",
    maximum=80,
    value=0,
    mode="determinate")
my_gauge.pack(pady=50, fill=X, padx=20)

start_button = tb.Button(
    root,
    text="Iniciar",
    bootstyle="success, outline",
    width=20,
    command=starter)
start_button.pack(pady=20)

stop_button = tb.Button(
    root,
    text="Parar",
    bootstyle="danger, outline",
    width=20,
    command=stoper)
stop_button.pack(pady=20)

increment_button = tb.Button(
    root,
    text="Adicionar",
    bootstyle="warning, outline",
    width=20,
    command=incrementer)
increment_button.pack(pady=20)

my_label = tb.Label(root, text="Posição: ")
my_label.pack(pady=20)

root.mainloop()