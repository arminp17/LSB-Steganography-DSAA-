from steglib import *
from AESCrypt import *
from compress import *
import time

filename = input("Enter filename(with extention):")
password = input("Enter password: ")
t_start = time.process_time()
restored_message=rand_LSBdecode(filename,password)
restored_message=decrypt(restored_message.encode("utf8"),password).decode("utf8")
restored_message = decompress(restored_message)
t_end = time.process_time()
print("Restored Message: ")
print(restored_message[:20],"......................contd")
print ("time taken = " + str(1000*(t_end - t_start)) + "ms")

outputfile = open(filename.split(".")[0]+"_restoredtext.txt","w")
outputfile.write(restored_message)
outputfile.close()
