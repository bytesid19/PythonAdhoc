#!/usr/bin/python2

#import is a keyword to import any python library
import time
import math   # theano --supercomputing --DL
import os #to understand and user Base os features/commands

print "preprocessing .......... ()()()"

voice="echo processing | festival --tts"	 #festival is a text-to-speech converter
# here system is a function under os library to run any command
os.system(voice)


time.sleep(5) #here 5 is second

#all data will be converted into string
x=raw_input('plz enter a number : ')
print type(x)
print x

dir(time) # time library me kya kya function hai display ho jaega


