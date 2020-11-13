from tkinter import *
from tkinter import messagebox as mb


window = Tk()

medFlu = 350
medCan = 400 

sckcde = Entry(window, width=20)
drtretmnt = Entry(window, width=10)
panum = Entry(window, width=20)
scfee = Entry(window, width=20)
scklb = Label(window, text="Sickness Cod:")
drtretlb = Label(window, text="Duration of Treatment:")
pnumlb = Label(window, text="Dr Practice code:")
scfeelb = Label(window, text="Fee/Consultation:")
wklb = Label(window, text="Weeks/Months")
amntlb = Label(window)

rvar = StringVar()

def selected_sickness():
    if rvar.get() == "Flu":
        if int(scfee.get()) >= 600:
            flutot = medFlu + int(scfee.get())
            amntlb.config(text="Total:" + str(flutot))
        if int(scfee.get()) < 600:
            flutot = medFlu + int(scfee.get())
            disflu = (flutot * (2/100)) + flutot
            mb.showinfo("message", "you got a discount of 2%")
            amntlb.config(text="Total" + str(disflu))
    if rvar.get() == "Cancer":
        if int(scfee.get()) > 600:
            mb.showinfo("Message", "Sorry we cant treat you")
        if int(scfee.get()) < 600:
           canTot = int(scfee.get()) + medCan
           amntlb.config(text="Total:" + str(canTot))

def clr():
    amntlb.config(text="")
    sckcde.delete("0",END)
    drtretmnt.delete("0",END)
    panum.delete("0",END)
    scfee.delete("0",END)

def ex():
    window.destroy()

exbtn = Button(window, text="exit", command=ex)
clrbtn = Button(window, text="clear", command=clr)
btn = Button(window, text="Calculate", command=selected_sickness)
radcan = Radiobutton(window, text="Cancer", variable=rvar,value="Cancer")
radin = Radiobutton(window, text="Influenza", variable=rvar, value="Flu")


scklb.grid(row=0, column=0, sticky=W)
drtretlb.grid(row=1, column=0, sticky=W)
scfeelb.grid(row=2, column=0, sticky=W)
pnumlb.grid(row=3, column=0, sticky=W)
wklb.grid(row=1, column=3)
sckcde.grid(row=0, column=1)
drtretmnt.grid(row=1, column=1)
scfee.grid(row=2, column=1)
panum.grid(row=3, column=1)
radcan.grid(row=4, column=0)
radin.grid(row=5, column=0)
amntlb.grid(row=6, column=0)
btn.grid(row=7, column=0)
clrbtn.grid(row=7, column=1)
exbtn.grid(row=7, column=2, sticky=E)
window.mainloop()