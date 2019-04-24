import time

start_time,current_time=time.clock() #starter tick
while current_time-start_time>60: # mainloop
    current_time=time.clock()
    print (current_time)
