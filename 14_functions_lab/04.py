"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""
def longer_than(num,*words):
    return [word for word in words if len(word) > num]

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')