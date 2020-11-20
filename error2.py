from tkinter import *
from tkinter import messagebox
ourframe2 = Tk()


def status():
    ourframe2 = Tk()
    ourframe2.geometry("300x500")
    ourframe2.title("Error handling")

label3= Label(ourframe2, text="Please enter amount in your account")
label3.pack()
entry3 = Entry(ourframe2)
entry3.pack()
def check_message():
    if int(entry3.get())>=3000:
        messagebox.showinfo("My status","You qualify for the Malaysia trip.Congrats!")
    else:
         messagebox.showinfo("My status","Sorry you don't qualify")
button3 = Button(ourframe2,text="check Qualification",command=check_message)
button3.pack()




ourframe2.mainloop()
