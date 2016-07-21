"""
      _      _      _
   __(.)< __(.)> __(.)=
   \___)  \___)  \___)   

Python course - Verint
Week 3

"""

import re


def toCamelCase(word):
    if re.search(r'(\w+)_(\w+)', word):
        word = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), word)
        word = re.sub('_', '', word)
    return word

    
def fromCamelCase(word):
    if re.search(r'[a-z][A-Z]', word):
        word = re.sub(r'([A-Z])', lambda m:'_' + m.group(0).lower() , word)
    return word


print toCamelCase('no_more_shall_we_part')
print fromCamelCase('noMoreShallWePart')