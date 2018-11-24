import cv2
import numpy as np
from math import log10

def psnr(img1,img2):
    rows = img1.shape[0]
    cols = img1.shape[1]
    channels = img1.shape[2]
    diff = 0
    for ch in range(channels):
        for col in range(cols):
            for row in range(rows):
                #print("Looping----")
                diff = diff + (int(img1[row,col,ch])-int(img2[row,col,ch]))**2

    return 10*log10((255**2)/(diff/(rows*cols*ch)))

img1 = cv2.imread("cow.jpg")
img2=  cv2.imread("cow_out.png")
print(psnr(img1,img2))
