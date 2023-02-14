import time
import sys
import os
print("How much minute do you take to sleep ??(min:sec)")
def input_check():
    loop=True
    while loop==True:
        time_min=input(" >> ") 
        time_=time_min
        time_=time_.split(":")
        added=""
        for i in time_:
            i=str(i)
            added=added+" "+i
        f_trans_time=added
        try:
            time_min=int(added.replace(" ",""))
            loop=False
        except:
            print("Please re-enter time in required format")
            loop=True
        for i in time_:
            if(int(i)>60 or int(i)<0):
                print("Please re-enter time in required format")
                loop=True
    timer(time_,f_trans_time)
def timer(time_,f_trans_time):
    print(time_)
    for i in range(0, len(time_)):
        min=int(time_[0])*60
        sec=int(time_[1])
    totaltime=min+sec
    print(totaltime)
    for i in range(1,totaltime+1):
        time.sleep(1)
        print(i,end=", ",flush=True)
    os.system("shutdown /s /t 1")
    sys.exit()

input_check()