"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""
def ten(*nums):
    res = 0
    for n in nums:
        if type(n) != int: raise Exception("Type should be integer")
        res += n/10%10
    return res
    