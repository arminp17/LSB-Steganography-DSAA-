from steglib import *
from AESCrypt import *
import time

filename = input("Enter filename(with extention):")
password = input("Enter password: ")
t_start = time.process_time()
restored_message=decode(filename)
restored_message=decrypt(restored_message.encode("utf8"),password).decode("utf8")
t_end = time.process_time()
print("Restored Message: ")
print(restored_message)
print ("time taken = " + str(1000*(t_end - t_start)) + "ms")
