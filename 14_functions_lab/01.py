"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""

def mysum(*arg):
    res = sum([n for n in arg if type(n) == int])
    return res

def mymul(*arg):
    res = 1
    for n in arg:
        if type(n) == int:
            res *= n
    return res

print mysum(401,202,202)