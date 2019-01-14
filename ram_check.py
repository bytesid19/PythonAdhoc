#!/usr/bin/env python2

import commands

ram=commands.getoutput("free -m")
fin_memory=ram.split()[7]
print "MY system RAM is "+fin_memory+" MB"
cpu=commands.getoutput("lscpu")
fin_cpu=cpu.split('\n')[12].split(':')[1]
print "MY system CPU is "+fin_cpu
