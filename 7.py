# TU DIEN
tong, tich = 0, 1
k = int(input())
if k <= 10:
    for i in range(k):
        try:
            key, value = input().split()
            value = int(value)
            tong += value
            tich *= value
        except:
            pass

    print(f"{tong} {tich}")
else:
    print("INVALID INPUT")

''' 
4
a 9
b 5
c abc
d 1
'''
