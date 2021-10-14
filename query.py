from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import os
import wget
from PIL import Image

import gplayer

#import display # local class

downloadPath = os.getcwd() + "\\IDR033_latestweather\\"
mapPath = os.getcwd() + "\\IDR033_map\\"
gifPath =  os.getcwd() + "\\weather\\"

hostname = "your proxy address"
port = "put your port here"
downloadPreferences = {"download.default_directory": downloadPath, "directory_upgrade": True}

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--headless') # nolonger works with BOM as they put bot detection
#options.add_argument('--proxy-server=%s' % hostname + ":" + port) # add a proxy connection
options.add_experimental_option("prefs", downloadPreferences)

driver = webdriver.Chrome(chrome_options=options)

woolongongURL = "http://www.bom.gov.au/products/IDR033.loop.shtml"
terryHillsURL = "http://www.bom.gov.au/products/IDR714.loop.shtml"

snapshots = []

# Set to wollongong for now since terry hills is down.
# TODO add parfam flag
driver.get(woolongongURL)

# Take 6 snapshots in 2 seconds to get every image

x = 0 # dont need x but whatever
for x in range(0, 20):
	snapshots.append(driver.page_source)
	print("Taken snapshot: {}".format(x))
	time.sleep(0.5)

# run through all of the snapshots and get the loop images.
imgURLS = []

i = 0
for i in range(0, 20):
	soup = BeautifulSoup(snapshots[i], features="html.parser")
	img = soup.findAll("img") 

	for image in img:
		imgs = image.get("src")
		
		if "IDR033" in imgs: # woolongong loop
			print("Found:" + imgs)
			imgURLS.append(imgs)

		elif "IDR714" in imgs: # terry hills loop
			print("Found:" + imgs)
			imgURLS.append(imgs)

# download and crop the images

for img in imgURLS:
	driver.get(img)
	driver.save_screenshot("temp.png")

	im = Image.open("temp.png")
	width, height = im.size   # Get dimensions

	left = (width - 512) / 2
	top = (height - 512) / 2
	right = (width + 512) / 2
	bottom = (height + 512) / 2

	# Crop the center of the image
	im = im.crop((left, top, right, bottom))
	im.save(downloadPath + "\\{}".format(img[28:]))

driver.close()


def gen_frame(path, bg):

    im = Image.open(path)
    alpha = im.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

    # Paste the color of index 255 and use alpha as a mask

    im.paste(255, mask)
   
    # The transparency index is 255
    im.info['transparency'] = 255

    bg.paste(im, (0, 0), im)

    return bg 


background = Image.open(mapPath + "IDR033_complete.png")

im1 = gen_frame(downloadPath + "IDR033.T.202110140504.png", background)
im2 = gen_frame(downloadPath + "IDR033.T.202110140509.png", background)     
im1.save("{}{}.gif".format(gifPath, time.time()), save_all=True, append_images=[im2], loop=5, duration=200)