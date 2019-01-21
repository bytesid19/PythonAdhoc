#!usr/bin/env python2

import socket

rec_ip="127.0.0.1" #same machine ke liye local ip nai toh receiver ka ip
rec_port=9090 # port>6000 are generally free to use

#calling udp protocol 
# socket.AF_INET--->ipv4 , socket.SOCK_DGRAM ---> UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#################################### above part is common to sender and receiver
while True:
	#it will send data to rec as well as create own socket(own ip  and any random port)
	data=raw_input("Enter your message : ")
	s.sendto(data,(rec_ip,rec_port)) #bhjta hai khud ka ip port sendto function ka kaam hai
	print s.recvfrom(10)
