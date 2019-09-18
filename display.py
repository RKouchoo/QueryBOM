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

images = [imageBackground, imageTopography, imageRange, imageWeather, imageLocations]

composite = Image.new("RGBA", (512, 512))

for im in images:
	composite = Image.alpha_composite(composite, im)

convertedComposite = ImageTk.PhotoImage(composite)

panel = Label(root, image=convertedComposite)
panel.grid(row=0, column=0, sticky=E)

root.mainloop()  # Start the GUI