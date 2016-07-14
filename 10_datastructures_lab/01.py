"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""

import sys
home = {}

with open('hosts.txt', 'r') as f:
    for line in f:
        fields = line.split("=")
        if len(fields) != 2 : continue
        (host,ip) = fields
        ip = ip.strip('\n')
        home[host] = ip

i = len(sys.argv)

for i in range(1,i):
    if sys.argv[i] in home:
        print home[sys.argv[i]]
    else:
        print "Error, host:" ,sys.argv[i] ,"not exist"
