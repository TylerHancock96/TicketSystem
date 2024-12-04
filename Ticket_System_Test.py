# Import Module
import sys
import tkinter
from tkinter import *

# Create root window
root = Tk()

# Root window title and dimensions
root.title("HTS")
# Set Geometry (widthxheight)
root.geometry('900x900')

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
# def clicked():
#    res = "You wrote " + txt.get()
#   lbl.configure(text=res)


# Define close button
def progclose():
    sys.exit()


# All widgets will be here

# Showing and hiding initial widgets
def show_widget():
    lbl.configure(text="Please describe your issue: ")
    txt = tkinter.Text(root, height=20, width=40)
    txt.grid(column=1, row=1)
    b1.grid_remove()
    CloseBtn.configure(text="Close", command=progclose)
    CloseBtn.grid(column=3, row=5)
    b1_cont.grid(column=1, row=4)


# Button to continue program
# Button with red text
b1 = Button(root, text="Yes", fg="red", command=show_widget)
# Button Grid
b1.grid(column=2, row=0)

# Button to close program
CloseBtn = Button(root, text="No", fg="blue", command=progclose)
# Button Grid
CloseBtn.grid(column=3, row=0)


# Block of code to show next phase of system
def phase_two():
    lbl.configure(text="Please upload any pictures/videos to better describe your issue if you have any")


b1_cont = Button(root, text="Continue", command=phase_two)

# Execute Tkinter
root.mainloop()
