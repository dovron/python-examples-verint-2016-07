"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""
def longer_than(num,*words):
    res = []
    for n in words:
        if len(n) > num:
            res.append (n)
    return res   

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')