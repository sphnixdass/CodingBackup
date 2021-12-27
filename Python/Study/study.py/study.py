from tkinter import *
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *


import time
root = Tk()
root.title("Study Dass")

f = open("currentrow.txt", "r")
#print(f.read()) 


icount = int(f.read())

with open('TheJungleBook.txt') as f:
    lines = [line.rstrip() for line in f]

# f = open("TheJungleBook.txt", "r")
# x = f.readline()
# print(x[5])
# f.close()


def upaterow():
    global icount
    f = open("currentrow.txt", "w")
    f.write(str(icount))
    f.close()

#print(f.readline())

def callbacksingleclick(event):
    global icount
    # print ("clicked at", event.x, event.y)
    icount = icount + 1
    var.set(lines[icount])
    label.pack()
    upaterow()

def callbackdoubleclick(event):
    global icount
    # print ("clicked at", event.x, event.y)
    icount = icount - 2
    var.set(lines[icount])
    label.pack()
    upaterow()


root.wait_visibility(root)
root.wm_attributes('-alpha',0.7)
root.wm_attributes('-topmost', 'true')
frame = Frame(root, width=100, height=100)
frame.bind("<Double-Button-1>", callbackdoubleclick)
frame.bind("<Button-1>", callbacksingleclick)
var = StringVar()
label = Label( frame, textvariable=var, relief=RAISED, wraplength=250)
label.bind("<Double-Button-1>", callbackdoubleclick)
label.bind("<Button-1>", callbacksingleclick)
# Here the PDF is converted to list of images
#pages = convert_from_path('/data/Backup/ebooks/50-Tips-and-Tricks-for-MongoDB-Developers_001.pdf',size=(800,900))

frame.pack()


# def test():
#     for i in range(5):
#         var.set("Hey!? How are you doing?" + str(i))
#         time.sleep(1)
#         label.pack()

root.mainloop()
