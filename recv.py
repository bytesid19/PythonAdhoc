#!usr/bin/env python2

import socket

rec_ip="127.0.0.1"
rec_port=9090 # port>6000 are generally free to use

#calling udp protocol 
# socket.AF_INET--->ipv4 , socket.SOCK_DGRAM ---> UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#################################### above part is common to sender and receiver

#rec side only
# bindin ip and port

s.bind((rec_ip,rec_port)) #tuple

while True : 
	#it will rec data from client / sender and its socket as well
	rec_data= s.recvfrom(100)
 	print "data is : "+rec_data[0]  # buffer size set kia sender 11 size bhjta hai toh receive bs 10 character hoga
#here rec_data[1] ka elemnts is client ip and client port combo
	rply=raw_input("enter yur rep : ")
	s.sendto(rply,rec_data[1])


