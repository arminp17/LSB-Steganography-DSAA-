from steglib import *
from AESCrypt import *
from compress import *
import time

filename = input("Enter filename(with extension):")
textfile = input("Enter text file name(with extension): ")
textfile = open(textfile,"r")
secret = textfile.read()
password = input("Set password: ")
t_start = time.process_time()
secret = compress(secret)
encrypted_secret=encrypt(secret,password).decode("utf8")
rand_LSBencode(filename,encrypted_secret,password)
t_end = time.process_time()
print ("time taken = " + str(1000*(t_end - t_start)) + "ms")
textfile.close()
