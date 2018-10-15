from steglib import *
import time

filename = input("Enter filename(with extention):")
t_start = time.process_time()
restored_message=decode(filename)
t_end = time.process_time()
print("Restored Message: ")
print(restored_message[0:100])
print ("time taken = " + str(1000*(t_end - t_start)) + "ms")
