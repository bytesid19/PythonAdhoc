#!/usr/bin/python

import webbrowser #web se interact krne ke liye library
import commands

#we can give a variable to comments like
options='''
Press 1 to check your OS version :
Press 2 to login your fb account : see selenium concept
Press 3 to check your RAM and CPU :
Press 4 to search something in google search engine :
Press 5 to list out all IP and mac address in your correct network zone : nmap se check krne ka approach hai 
'''

#unhandled key handle kro ki user 1-5 ke alawa kch daal hi nai paaye

print options

print "Enter your choice : "
choice=raw_input()
print "you have entered : ",choice

if int(choice) == 1 :
	print "MY OS is RHEL"

elif int(choice) == 3:
	execfile('ram_check.py')
	
elif int(choice) == 4 :
	data=raw_input("Type something to search in google : ")
	webbrowser.open_new_tab('https://www.google.com/search?q='+data)

else :
	print "No valid option given"

#conditional statements
'''
if 3+2:
	print 'hi'
else:
	print 'no hi'

#python is called repl (read evaluate print loop)
'''

'''
library is a driver of python jisse apps,technology,os chala skte hai
selenium dekho for login in fb accnt
'''
