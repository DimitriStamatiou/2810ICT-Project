#import the libraries + other files in the project
import tkinter as tk
from tkinter.ttk import *
from search import *

#UI variables go here
var = "1"
#UI Functions
def Listings():
    search = query.get()
    label = tk.Label(text = Listing(search), bg = secColour)
    label.place(x = 0, y = 100)
def Reviews():
    search = query.get()
    label = tk.Label(text = Review(search), bg = secColour)
    label.place(x = 100, y = 100)
def Suburbs():
    search = query.get()
    label = tk.Label(text = Suburb(search), bg = secColour)
    label.place(x = 0, y = 100)
def Date():
    search = query.get()
    label = tk.Label(text = Dates(search), bg = secColour)
    label.place(x = 200, y = 100)

    #I'm drawing this window here, because it doubled up in the other script
    options = tk.Tk()
    options.resizable(False, False)
    options.title("Test")
    label = tk.Label(options, text = "Would you like to draw a graph?")
    label.pack()
    ybut = tk.Button(options, text = "Yes", command = Yes)
    ybut.pack()
    nbut = tk.Button(options, text = "No", command = No)  
    nbut.pack()
    options.mainloop()
#drawing the GUI
root = tk.Tk()
root.title("GUI")

bgColour = "red"
secColour = "orange"

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

width = 1000
height = 400

centerX = int(screenWidth / 2 - width / 2)
centerY = int(screenHeight / 2 - height / 2)

root.geometry(f'{width}x{height}+{centerX}+{centerY}')
root.resizable(False, False)

frame1 = tk.Frame(master = root,height = height, bg = bgColour)
frame1.pack(fill = tk.X)

label = tk.Label(text = "Search:", bg = bgColour)
query = tk.Entry(root)
Lbutton = tk.Button(text = "Search Listings", bg = secColour, command = Listings)
Lbutton.place(x = 230, y = 0)

Rbutton = tk.Button(text = "Search Reviews", bg = secColour, command = Reviews)
Rbutton.place(x = 370, y = 0)

Sbutton = tk.Button(text = "Search Suburbs", bg = secColour, command = Suburbs)
Sbutton.place(x = 510, y = 0)

Dbutton = tk.Button(text = "Search Dates", bg = secColour, command = Date)
Dbutton.place(x = 650, y = 0)
label.place(x = 0, y = 0)
query.place(x = 60, y = 0)

root.mainloop()
