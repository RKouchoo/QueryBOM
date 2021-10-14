from PIL import Image
import os
import time
import cv2

import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

downloadPath = os.getcwd() + "\\IDR033_latestweather\\"
mapPath = os.getcwd() + "\\IDR033_map\\"
gifPath =  os.getcwd() + "\\weather\\"


def gen_frame(path):

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

    return im 



def combine(im, bg):

    bg.paste(im)

    return(bg)



def  removeBlack(file):
    src = cv2.imread(file, 1)
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) 
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)

    while True:
        cv2.imshow(dst)

    #cv2.imwrite(gifPath + "test.png", dst)


removeBlack(downloadPath + "IDR033.T.202110140504.png")


#background = Image.open(mapPath + "IDR033_complete.png")

#im1 = gen_frame(downloadPath + "IDR033.T.202110140504.png")

#im2 = gen_frame(downloadPath + "IDR033.T.202110140509.png")     


#ims = combine(background, im1)

#ims.save("{}{}.png".format(gifPath, "test"))


#im1.save("{}{}.gif".format(gifPath, time.time()), save_all=True, append_images=[im2], loop=5, duration=200)