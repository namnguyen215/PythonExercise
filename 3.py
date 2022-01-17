# COVID-19 DELTA

def run(n: int):
    tmp = n // 11
    result = 2**tmp - 1
    return result


n = int(input())
if n > 10 or n < 0:
    print("INVALID INPUT")
for _ in range(n):
    num = int(input())
    if num > 365:
        print("INVALID INPUT")
    else:
        print(run(num))

''' 
5
7
380
18
113
30
'''
