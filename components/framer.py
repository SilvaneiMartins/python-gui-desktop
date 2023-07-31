from tkinter import *
from datetime import date
from ttkbootstrap.dialogs import Querybox

import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("Framer")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

def thing():
    my_label.config(text=f"Você clicou em: {my_entry.get()}") 

my_frame = tb.Frame(
    root,
    bootstyle="light")
my_frame.pack(pady=20)

my_entry = tb.Entry(
    my_frame,
    font=("Poppins", 18))
my_entry.pack(pady=20)

my_button = tb.Button(
    my_frame,
    text="CLicar Aqui...",
    bootstyle="dark",
    command=thing)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(
    root,
    text="Silvanei martins",
    font=("Poppins", 18),
    bootstyle="inverse light")
my_label.pack(pady=20)

root.mainloop()