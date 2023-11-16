import os
import tkinter

os.environ['DISPLAY'] = ':0.0'  # X11 forwarding setup

window = tkinter.Tk()
window.title("My Window")
window.geometry("500x350")

my_label = tkinter.Label(window, text="Hello World", font="DejaVuSerif 18")
my_label.grid(row=0, column=0)

window.mainloop() #This is the last line of code in your program