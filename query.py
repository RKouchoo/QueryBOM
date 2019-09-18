from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import wget

import display # local class

hostname = "proxy.tafensw.edu.au"
port = "8080"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--proxy-server=%s' % hostname + ":" + port) # this doesnt seem to work sometimes on tafe/uni wifi

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

driver.close()

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