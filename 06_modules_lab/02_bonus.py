"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 1

"""
from colorama import Fore,init
import sys

init()

i = sys.argv

if len(i)!=3: 
    print Fore.RED + 'Error!'
    print Fore.RESET + "pleae enter 2 number"
else:
    try:
        i = int(sys.argv[1]) + int(sys.argv[2])
        print "The sum of the numbers is:",i
    except sys.exit("Error, text is not valid - Please enter a number"):
        print