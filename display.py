from tkinter import *
from PIL import Image, ImageTk
from os import path

root = Tk()  # A root window for displaying objects
# open image
imageHead = Image.open(path.relpath('IDR033_map/IDR033_backround.png'))
imageHand = Image.open(path.relpath('IDR033_weather/weather1.png'))

imageHead.paste(imageHand, (512, 512), imageHand)
# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(imageHead)

panel1 = Label(root, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)
root.mainloop()  # Start the GUI