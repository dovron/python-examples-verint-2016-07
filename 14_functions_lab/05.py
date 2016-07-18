"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""
from collections import defaultdict

def groupby(func, *args):
      dict = defaultdict(list)
      for n in args:
            dict[func(n)].append(n)
      return dict

print groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')