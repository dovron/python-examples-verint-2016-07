"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""

def mysum(*arg):
    res = 0
    for n in arg:
        if type(n) == int:
            res += n
    return res

def mymul(*arg):
    res = 1
    for n in arg:
        if type(n) == int:
            res *= n
    return res
