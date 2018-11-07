import cv2
import numpy
from randomseqgen import *

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
def rand_LSBencode(filename,secret,password):
    print("Initializing Encoding: ")
    img = cv2.imread(filename);
    print("Dimensions of image:")
    print(img.shape)
    rows = img.shape[0]
    cols = img.shape[1]
    channels = img.shape[2]
    secret = secret + chr(3) ##Added Delimiter
    binsequence = generate_bin_sequence(secret)
    #print("Binary Secret: "+binsequence)
    if len(binsequence)>img.size:
        print("Image too Small for given input data")
        return
    maxcount = len(binsequence)
    count=0
    set_seed(password)
    mod_list=gen_rand_sequence(maxcount+(maxcount)//10,rows,cols,channels)
    for pixel_address in mod_list:
        print(pixel_address)
        if count==maxcount:
            cv2.imwrite(filename.split(".")[0]+"_out.png",img)
            return
        val=img[pixel_address[0],pixel_address[1],pixel_address[2]]
        img[pixel_address[0],pixel_address[1],pixel_address[2]]=modifyval(val,binsequence[count])
        count+=1

def rand_LSBdecode(filename,password):
    img = cv2.imread(filename);
    rows = img.shape[0]
    cols = img.shape[1]
    channels = img.shape[2]
    bin_sequence=""
    set_seed(password)
    maxcount = rows*cols*channels
    mod_list=gen_rand_sequence(maxcount+(maxcount)//10,rows,cols,channels)[0:maxcount]
    bitcount=0
    for pixel_address in mod_list:
        val=img[pixel_address[0],pixel_address[1],pixel_address[2]]
        bin_sequence=bin_sequence+str(val%2)
        if bitcount==7:
            if int(bin_sequence[-8:],2)==3:
                break
            bitcount=0
        bitcount+=1
        
    binlist=[bin_sequence[i:i+8] for i in range(0, len(bin_sequence), 8)]
    restored_message=""
    for byte in binlist:
        bytenum = int(byte,2)
        if bytenum==3:
            break
        if bytenum>31:
            restored_message = restored_message + chr(bytenum)

    return restored_message
