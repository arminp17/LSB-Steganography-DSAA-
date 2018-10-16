from steglib import *
import time
filename = input("Enter filename(with extention):")
secret = input("Enter secret Message: ")
t_start = time.process_time()
encode(filename,secret)
t_end = time.process_time()
print ("time taken = " + str(1000*(t_end - t_start)) + "ms")
