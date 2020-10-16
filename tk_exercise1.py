import tkinter
from tkinter import *

window  = Tk()
window.geometry("300x200")
window.title("Adding two numbers")


myLabel = Label(window,text = ("Please enter first number"))
myLabel = Label(window , text = ("Please enter second number"))
myLabel = Label(window,text=("Your answer"))

btn = tkinter.Button(window,text="Add")
btn = tkinter.Button(window,text="clear")
btn = tkinter.Button(window,text="exit")

myLabel.pack()
btn.pack()