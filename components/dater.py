from tkinter import *
from datetime import date
from ttkbootstrap.dialogs import Querybox

import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("Date Entry")
root.iconbitmap("images/logo.png")
root.geometry("800x500")

def get_date():
    my_label.config(text=f"Sua data: {my_date.entry.get()}")

def get_calendar():
    cal = Querybox()
    my_label.config(text=f"Seu calendário: {cal.get_date()}")

my_date = tb.DateEntry(
    root, 
    bootstyle="danger",
    firstweekday= 0,
    startdate=date(2023, 7, 31))
my_date.pack(pady=20)

my_button = tb.Button(
    root, 
    text="Pegar Data", 
    bootstyle="danger outline",
    command= get_date)   
my_button.pack(pady=20)

my_button2 = tb.Button(
    root, 
    text="Pegar Calendário", 
    bootstyle="success outline",
    command= get_calendar)   
my_button2.pack(pady=20)

my_label = tb.Label(root, text="")
my_label.pack(pady=20)

root.mainloop()