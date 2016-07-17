"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 2

"""
def wrong_types(int_type, str_type):
    if type(int_type) is not int: raise Exception("Type should be integer")
    if type(str_type) is not str: raise Exception("Type should be srting")