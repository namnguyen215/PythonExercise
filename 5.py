# TONG TICH LUY

n = int(input())
arr = [int(num) for num in input().split()]
tmp_arr = arr.copy()
tich = arr[0]
for i in range(1, n):
    tmp_arr[i] = tmp_arr[i-1] + arr[i]
    tich *= tmp_arr[i]

print(f"{sum(tmp_arr, 0)} {tich}")

''' 
3
1 2 3
'''