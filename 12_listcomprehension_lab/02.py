"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2
ver 2
"""

letter = [chr(i) for i in range(ord('a'),ord('z'))]

word = [ x + y + z for x in letter for y in letter for z in letter]

print word
