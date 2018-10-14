import cv2
import numpy


def decode(filename):
    img = cv2.imread(filename);
    rows = img.shape[0]
    cols = img.shape[1]
    channels = img.shape[2]
    bin_sequence=""
    for ch in range(channels):
        for col in range(cols):
            for row in range(rows):
                val=img[row,col,ch]
                bin_sequence=bin_sequence+str(val%2)
    print(bin_sequence[0:240])            

filename = input("Enter filename(with extention):")
decode(filename)
