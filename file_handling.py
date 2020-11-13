from tkinter import *

#Renaming tkinter and changing miscellaneous window data
root = Tk()
root.title("Text Files")
root.geometry('600x500')
root.configure(bg='red')

#This class contains the program
class weekendActivities:
    def __init__(self):
        #creating label and textbox
        heading = Label(root, text="My weekend activities", font=('Helvetica', 20), bg='red')
        self.display_text = Text(root, height=16, width=60,borderwidth=0, bg='red')
        self.display_text.config(highlightbackground="red")
        self.box = Text(root, height=7, width=60)

        #creating buttons
        create_button= Button(root, text="Create textfile", command=self.create)
        display_button = Button(root, text="Display", command=self.display)
        append_button = Button(root, text="Append data", command=self.append)
        clear_button = Button(root, text="Clear", command=self.clear)
        exit_button = Button(root, text="Exit", command=root.destroy)

        #label and text placements
        heading.place(x=50, y=50)
        self.display_text.place(x=50, y=280)
        self.box.place(x=50, y=90)

        #button placements
        create_button.place(x=45,y=235)
        display_button.place(x=175,y=235)
        append_button.place(x=260,y=235)
        clear_button.place(x=380,y=235)
        exit_button.place(x=450,y=235)


    #Modules(functions) for the buttons' instructions after clicked
    def create(self):
        f=open("myweekend.txt", "w+")
        f.write(self.box.get("1.0", END))
        f.close()

    def display(self):
        f=open("myweekend.txt", "r+")
        self.display_text.insert(END, f.read())

    def append(self):
        f=open("myweekend.txt", "a+")
        f.write(self.box.get("1.0", END))
        f.close()

    def clear(self):ZA

        self.box.delete("1.0", END)
        self.display_text.delete("1.0", END)
        
#running class weekend and allowing tkinter to loop
run = weekendActivities()
root.mainloop()
			
			
			