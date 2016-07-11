"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""

import sys

with open(sys.argv[1], "r") as fin:
    with open(sys.argv[2], "a") as fout:
        fout.write("\n")                
        for line in fin:
            fout.write(line)