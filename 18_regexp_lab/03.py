"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 3

"""

import re
import sys


with open(sys.argv[1], 'r') as f:
    for line in f:
        word = re.sub(r'(\w+),(\w+)', lambda m: m.group(2) + ',' + m.group(1) , line)
        print word