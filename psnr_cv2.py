import cv2
import numpy as np
from math import log10
import os

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



filelist=[]
dir = "tests"
for file in os.listdir(dir):
    if file.endswith(".jpg"):
        filelist.append(os.path.join(dir, file))

for file in filelist:
    img1 = cv2.imread(file)
    img2=  cv2.imread(file.split(".")[0]+"_out.png")
    print(file + "  ::::: PSNR: "+str(psnr(img1,img2)))
