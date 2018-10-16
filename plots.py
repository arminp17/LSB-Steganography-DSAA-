from steglib import *
import matplotlib.pyplot as plt
'''img = cv2.imread("cow.jpg")
img_enc = cv2.imread("cow_out.png")
img_arr=numpy.empty((0))
img_enc_arr=numpy.empty((0))

rows = img.shape[0]
cols = img.shape[1]
channels = img.shape[2]

for col in range(10):
    for row in range(rows):

        img_arr=numpy.append(img_arr,[int(img[row,col,0])],axis=0)
        img_enc_arr=numpy.append(img_enc_arr,[img_enc[row,col,0]],axis=0)


print(img_arr)
plt.stem(img_arr[0:50])
plt.xlabel("Image Before encoding")
plt.show()

plt.stem(img_enc_arr[0:50])
plt.xlabel("Image After encoding")
plt.show()

plt.stem(abs(img_arr[0:50]-img_enc_arr[0:50]))
plt.xlabel("Difference Between images")
plt.ylim(-1,220)
plt.show()

bin="0100100001100101011011000110110001101111"
binlist=[int(bin[i]) for i in range(len(bin))]
plt.stem(binlist)
plt.xlabel("Signal Representation for Secret : Hello")
plt.show()
'''
timelist=[15.625,15.625,46.875,46.875,93.75,156.25,234.375]
dimlist=[50,100,250,500,1000,1500,2000]
plt.plot(dimlist,timelist)
plt.xlabel("Dimensions of image")
plt.ylabel("Time Taken to ENCODE")
plt.show()
