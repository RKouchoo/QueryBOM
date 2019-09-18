from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import os
import wget
from PIL import Image

#import display # local class

downloadPath = os.getcwd() + "\\IDR033_latestweather\\"

hostname = "proxy.tafensw.edu.au"
port = "8080"
downloadPreferences = {"download.default_directory": downloadPath, "directory_upgrade": True}

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
#options.add_argument('--proxy-server=%s' % hostname + ":" + port) # this doesnt seem to work sometimes on tafe/uni wifi
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
for x in range(0, 5):
	snapshots.append(driver.page_source)
	print("Taken snapshot: {}".format(x))
	time.sleep(0.333)

# run through all of the snapshots and get the loop images.
imgURLS = []

i = 0
for i in range(0, 5):
	soup = BeautifulSoup(snapshots[i])
	img = soup.findAll("img") 

	for image in img:
		imgs = image.get("src")
		
		if "IDR033" in imgs: # woolongong loop
			print("Found:" + imgs)
			imgURLS.append(imgs)

		elif "IDR714" in imgs: # terry hills loop
			print("Found:" + imgs)
			imgURLS.append(imgs)

# download the images

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
	im.save(downloadPath + "\\{}.png".format(img[28:]))

driver.close()
