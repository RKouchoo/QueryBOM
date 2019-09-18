from bs4 import BeautifulSoup
import requests
import selenium
import time
import display

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
#options.add_argument('--proxy-server="https://proxy.tafensw.edu.au"') # this doesnt seem to work on tafe/uni wifi. Not sure why

driver = webdriver.Chrome(chrome_options=options)

woolongongURL = "http://www.bom.gov.au/products/IDR033.loop.shtml"
terryHillsURL = "http://www.bom.gov.au/products/IDR714.loop.shtml"

snapshots = []

# Set to wollongong for now since terry hills is down.
driver.get(woolongongURL)

# Take 6 snapshots in 2 seconds to get every image

x = 0 # dont need x but whatever
for x in range(0, 5):
	snapshots.append(driver.page_source)
	print("Taken snapshot: {}".format(x))
	time.sleep(0.333)

driver.close()

#r = requests.get(woolongongURL) #, proxies=proxyDict)
#html = r.text

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


