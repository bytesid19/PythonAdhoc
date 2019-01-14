#!/usr/bin/python

'''
free -m
import commands
dir(commands) - have functions
commands.getoutput('') - python os se directly interact krga is command se
'''

import commands

ram=commands.getoutput("free -m")
print ram
