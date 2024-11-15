# Import Module
import sys
from tkinter import *

# Create root window
root = Tk()

# Root window title and dimensions
root.title("HTS")
# Set Geometry (widthxheight)
root.geometry('350x200')

# Add menu bar
# new item in menu bar labeled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# Adding a label to the root window
lbl = Label(root, text="Do you need IT help?")
lbl.grid()


# Function to display text when button is clicked
def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text=res)


# Define close button
def progclose():
    sys.exit()


# Adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)


# All widgets will be here
# Showing and hiding widgets
def show_widget():
    txt.pack()


def hide_widget():
    txt.pack_forget()
    b1.configure(command=hide_widget)


# Button to continue program
# Button with red text
b1 = Button(root, text="Yes", fg="red", command=show_widget)
# Button Grid
b1.grid(column=2, row=0)

# Button to close program
CloseBtn = Button(root, text="No", fg="blue", command=progclose)
# Button Grid
CloseBtn.grid(column=3, row=0)

# Execute Tkinter
root.mainloop()
