import cv2
import numpy


dimlist=[50,100,250,500,1000,1500,2000]
for dim in dimlist:
    Z = numpy.random.randint(0,high=255,size=(dim,dim,3))   # Test data
    cv2.imwrite(str(dim)+".png",Z)
