"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""

def sum_nums(*arg):
    res = 0
    for n in arg:
        if type(n) == int:
            res += n
    return res

def mul_nums(*arg):
    res = 1
    for n in arg:
        if type(n) == int:
            res *= n
    return res


print sum_nums(941,'a',100,100,1001,100)
print mul_nums('foo', 'bar', 10, 20)