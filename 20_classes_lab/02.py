"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 3

"""

class MyCounter(object):
    count = 0

    def __init__(self):
        MyCounter.count += 1


for _ in range(10):
     c1 = MyCounter()

# should print 10
print MyCounter.count
