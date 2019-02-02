

import  socket
import thread

rec_ip="127.0.0.1"
rec_port=9090   
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  sending  messag to target 
def one():
    while  True:
        data=raw_input("type your command  :  ")
        s.sendto(data,(rec_ip,rec_port))
        print " "

def two():
    while True:
        print s.recvfrom(100)

thread.start_new_thread(one,())
thread.start_new_thread(two,())

while True:
    pass
	
