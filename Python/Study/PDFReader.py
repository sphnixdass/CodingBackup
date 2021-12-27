from tkinter import *
from tkinter import ttk
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import locale
import ghostscript
from gtts import gTTS 
import os
import threading


pdffilepath = "/data/Backup/ebooks/Genetic Algorithms with Python by Clinton Sheppard (z-lib.org).pdf"
driver = webdriver.Firefox(executable_path="/usr/local/share/gecko_driver/geckodriver")
driver.get("file://" + pdffilepath + "#page=1")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

pagenumber = 1

root = Tk()
root.title("Study Dass")
labelvar = StringVar()

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


def playvideo():
    global pagenumber
    print("called play video start")
    # os.system("ffplay -nodisp -autoexit welcome.mp3") 
    os.system("vlc --rate=1.5 --play-and-exit welcome.mp3") 
    print("called play video start")
    pagenumber = pagenumber + 1
    changepage()
    

def changepage():
    global pagenumber
    global monthchoosen
    print(monthchoosen.get())
    monthchoosen['values'] = (str(pagenumber - 5), str(pagenumber - 4), str(pagenumber - 3), str(pagenumber - 2), str(pagenumber - 1), str(pagenumber), str(pagenumber + 1), str(pagenumber + 2), str(pagenumber +3 )) 
    driver.get("file://" + pdffilepath + "#page=" + str(pagenumber))
    args = [
        "gs", # actual value doesn't matter
        "-dNOPAUSE", "-dBATCH", "-dSAFER",
        "-sDEVICE=txtwrite",
        "-dFirstPage=" + str(pagenumber), "-dLastPage=" + str(pagenumber),
        "-sOutputFile=output.txt",
        "-q", pdffilepath
        ]

    # arguments have to be bytes, encode them
    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]

    ghostscript.Ghostscript(*args)
    ghostscript.cleanup()

    file1 = open("output.txt","r")
    outputtxt = file1.read()
    for k in range(1, 50):
        outputtxt = outputtxt.replace("  ", " ").replace('\n', ' ').replace('\r', '')
    
    print(outputtxt)
    file1.close()
    labelvar.set(outputtxt)
    monthchoosen.current(0)
    # Language in which you want to convert 
    language = 'en'
    
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=outputtxt, lang=language, slow=False) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3")
    t1 = threading.Thread(target=playvideo)
    t1.start()
    t1._stop()
    
    # Playing the converted file 






def callbackcomboselected(event):
    global monthchoosen
    global pagenumber
    pagenumber = int(monthchoosen.get())
    changepage()




root.wait_visibility(root)
root.wm_attributes('-alpha',0.7)
# root.wm_attributes('-topmost', 'true')

frame = ttk.Frame(root, width=100, height=100)
frame.bind("<Double-Button-1>", callbackdoubleclick)
frame.bind("<Button-1>", callbacksingleclick)


# Combobox creation 
n = StringVar() 
monthchoosen = ttk.Combobox(frame, width = 50, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = ('10', '20', '30', '40') 
monthchoosen.grid(column = 1, row = 1) 
monthchoosen.bind("<<ComboboxSelected>>", callbackcomboselected)
monthchoosen.current(0) 
label = ttk.Label( frame, textvariable=labelvar, relief=RAISED, wraplength=350)
# label.bind("<Double-Button-1>", callbackdoubleclick)
# label.bind("<Button-1>", callbacksingleclick)
label.grid(column = 1, row = 2) 

# Here the PDF is converted to list of images
#pages = convert_from_path('/data/Backup/ebooks/50-Tips-and-Tricks-for-MongoDB-Developers_001.pdf',size=(800,900))

frame.pack()


# def test():
#     for i in range(5):
#         var.set("Hey!? How are you doing?" + str(i))
#         time.sleep(1)
#         label.pack()

root.mainloop()
