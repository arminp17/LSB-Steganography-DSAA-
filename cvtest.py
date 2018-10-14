import cv2
import numpy as np
img = cv2.imread("red.png")
'''
cv2.imshow("imageB",img[:,:,0])
cv2.imshow("imageG",img[:,:,1])
cv2.imshow("imageR",img[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
imgcpy = img.copy()
#for i in range(len(imgcpy[:,:,2])):
print(imgcpy[:,:,2])

print((imgcpy[:,:,2][0,0]))
