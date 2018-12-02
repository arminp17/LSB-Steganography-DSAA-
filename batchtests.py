from steglib import *
from AESCrypt import *
from compress import *
import time
import os

filelist=[]
for file in os.listdir("tests"):
    if file.endswith(".jpg"):
        filelist.append(os.path.join("tests", file))

textfile = open('tests/secret.txt',"r")
secret = textfile.read()
secret = compress(secret)
password = "123"
encrypted_secret=encrypt(secret,password).decode("utf8")
textfile.close()
for file in filelist:
    print(file)
    t_start = time.process_time()
    rand_LSBencode(file,encrypted_secret,password)
    t_end = time.process_time()
    print (file + " ::time taken = " + str(1000*(t_end - t_start)) + "ms")
