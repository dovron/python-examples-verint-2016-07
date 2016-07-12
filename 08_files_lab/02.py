"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""

import sys
import binascii
from itertools import izip_longest

with open(sys.argv[1], "r") as fin1:
    with open(sys.argv[2], "r") as fin2:
        with open(sys.argv[3], "w") as fout:
            print >> fout, list(izip_longest(fin1,fin2,fillvalue=None))