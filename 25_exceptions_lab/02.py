"""
Python course - Verint
Week4

"""
import sys

i=0
try:
    with open(sys.argv[1], "r") as fin:
        for line in fin: i += 1
        print i
    
except Exception as e:
    print "Sorry, file %s not found" % (sys.argv[1])
