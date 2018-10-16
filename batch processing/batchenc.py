from steglib import *
import time
import string
import random
dimlist=[50,100,250,500,1000,1500,2000]
for dim in dimlist:
    secret=''.join([random.choice(string.ascii_letters + string.digits) for n in range(dim)])
    t_start = time.process_time()
    encode(str(dim)+".png",secret)
    t_end = time.process_time()
    print (str(dim)+"," + str(1000*(t_end - t_start)) + "ms")
