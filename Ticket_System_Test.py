# Import Module
import sys
from tkinter import *

# Create root window
root = Tk()

# Root window title and dimensions
root.title("HTS")
# Set Geometry (widthxheight)
root.geometry('350x200')
# Adding a label to the root window
lbl = Label(root, text = "Do you need IT help?")
lbl.grid()
# Function to display text when button is clicked
def clicked():
    res = "You wrote" + txt.get()
    lbl.configure(text=res)
# Define close button
def clickedClose():
    sys.exit()

# Adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)
# All widgets will be here

# Button to continue program
# Button with red text
btn = Button(root, text="Yes", fg="red", command=clicked)
# Button Grid
btn.grid(column=2, row=0)

# Button to close program
CloseBtn = Button(root, text="No", fg="blue", command=clickedClose)
# Button Grid
CloseBtn.grid(column=3, row=0)

# Execute Tkinter
root.mainloop()

if clicked():
    txt.grid(column=1, row=0)