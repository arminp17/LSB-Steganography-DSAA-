from steglib import *
import time
dimlist=[50,100,250,500,1000,1500,2000]
for dim in dimlist:
    t_start = time.process_time()
    restored_message=decode(str(dim)+"_out.png")
    t_end = time.process_time()
    print (str(dim)+"," + str(1000*(t_end - t_start)) + "ms")
