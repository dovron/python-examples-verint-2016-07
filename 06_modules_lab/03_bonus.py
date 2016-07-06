"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 1

"""

import os,sys
import argparse
from os.path import join, getsize

parser = argparse.ArgumentParser()
parser.add_argument("--Location", help="Location to delete")
parser.add_argument("--Size", help= "Min size for delete",type=int)

args = parser.parse_args()

size= 1000000
path= "."

if args.Location <> "None":
    path = args.Location

if args.Size <> "None":
    size = args.Size
print size

for root, dir, files in os.walk(path):
    for name in files:
        if getsize(join(root, name)) > size:
            print "Do you want to delete:" , join(root, name),"? [Y/N]"
            if raw_input() == ("Y"):
                os.remove(join(root, name))
