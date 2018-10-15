import cv2
import numpy
def dec2bin(dec):
    str="{0:b}".format(dec)
    return "0"*(8-len(str)) + str
def generate_bin_sequence(text):
    binsequence=""
    for char in text:
        binsequence = binsequence+dec2bin(ord(char))
    return binsequence

def modifyval(val,bit):
    if bit=="0" and val%2==1:
        val=val-1
    if bit=="1" and val%2==0:
        val=val+1
    return val
def encode(filename,secret):
    print("Initializing Encoding: ")
    img = cv2.imread(filename);
    print("Dimensions of image:")
    print(img.shape)
    rows = img.shape[0]
    cols = img.shape[1]
    channels = img.shape[2]
    binsequence = generate_bin_sequence(secret)
    print("Binary Secret: "+binsequence)
    if len(binsequence)>img.size:
        print("Image too Small for given input data")
        return
    maxcount = len(binsequence)
    count=0
    for ch in range(channels):
        for col in range(cols):
            for row in range(rows):
                if count==maxcount:
                    cv2.imwrite(filename.split(".")[0]+"_out.png",img)
                    return
                val=img[row,col,ch]
                img[row,col,ch] = modifyval(val,binsequence[count])
                count+=1

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

    binlist=[bin_sequence[i:i+8] for i in range(0, len(bin_sequence), 8)]
    restored_message=""
    for byte in binlist:
        bytenum = int(byte,2)
        if bytenum>31:
            restored_message = restored_message + chr(bytenum)

    return restored_message
