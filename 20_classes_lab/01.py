"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 3

"""

class Summer(object):

    def __init__(self):
        self.item = 0

    def add(self, *num):
        self.item += sum([n for n in num if type(n) == int])

    def total(self):
        return self.item

s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()