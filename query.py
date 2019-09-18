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

driver = webdriver.Chrome(chrome_options=options)

woolongongURL = "http://www.bom.gov.au/products/IDR033.loop.shtml"
terryHillsURL = "http://www.bom.gov.au/products/IDR714.loop.shtml"

# only used for testing since the network im on uses a proxy
proxyDict = {
  'https' : 'https://proxy.tafensw.edu.au:8080',
}

snapshots = []

# Set to wollongong for now since terry hills is down.
driver.get(woolongongURL)

# Take 6 snapshots in 2 seconds to get every image

x = 0 # dont need x but whatever
for x in range(0, 5):
	snapshots.append(driver.page_source)
	print("Taken snapshot: {}".format(x))
	time.sleep(0.33)

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
		if "IDR033" in imgs:
			print(imgs)
			imgURLS.append(imgs)
