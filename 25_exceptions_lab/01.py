""""
Python course - Verint
Week4

"""

import math

while True:
    line = raw_input()
    if not line: break

    try:
        print math.sqrt(int(line))
    
    except ValueError as e:
        print "please type a valid positive number"
