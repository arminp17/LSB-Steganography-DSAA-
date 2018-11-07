from steglib import *
from AESCrypt import *
import time

filename = input("Enter filename(with extention):")
secret = input("Enter secret Message: ")
password = input("Set password: ")
t_start = time.process_time()
encrypted_secret=encrypt(secret,password).decode("utf8")

rand_LSBencode(filename,encrypted_secret,password)
t_end = time.process_time()
print ("time taken = " + str(1000*(t_end - t_start)) + "ms")
