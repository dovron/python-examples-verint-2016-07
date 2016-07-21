"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 3

"""

import re
import sys

def config_param(file,word):
    with open(file, 'r') as f:
        for line in f:
            res = re.search(r'(\w+)\s*=\s(\w+)', line)
            if res.group(1) == (word):
                return res.group(2)

print config_param(sys.argv[1],sys.argv[2])