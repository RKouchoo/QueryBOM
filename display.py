from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()  # A root window for displaying objects

def loadImage(path):
	return Image.open(os.getcwd() + "\\" + path).convert("RGBA")

# open image
imageBackground = loadImage("IDR033_map\\IDR033_background.png")
imageLocations = loadImage("IDR033_map\\IDR033_locations.png")
imageRange = loadImage("IDR033_map\\IDR033_range.png")
imageTopography = loadImage("IDR033_map\\IDR033_topography.png")

imageWeather = loadImage("IDR033_latestweather\\weather1.png")


comp = ImageTk.PhotoImage(Image.alpha_composite(imageBackground, imageTopography))
comp = Image.alpha_composite(comp, ImageTk.PhotoImage(imageRange))
comp = Image.alpha_composite(comp, ImageTk.PhotoImage(imageWeather))
comp = Image.alpha_composite(comp, ImageTk.PhotoImage(imageLocations))

panel1 = Label(root, image=comp)
panel1.grid(row=0, column=0, sticky=E)

root.mainloop()  # Start the GUI