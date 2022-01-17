# HE SO JACCARD

import re

def run(a: list, b: list):
    s1 = set(a)
    s2 = set(b)
    result = float(len(s1.intersection(s2)) / len(s1.union(s2)))
    return result
    
a, b = input().lower(), input().lower()
a, b = re.findall('\w', a), re.findall('\w', b)
print(f"{run(a, b):.2f}")
''' 
hom nay thi lap trinh python
Lap trinh Python.
Hom qua troi mua.
Hom qua mua, ngay mai co nang khong?
'''
