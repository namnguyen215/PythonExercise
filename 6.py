# DANH SACH LONG NHAU
my_dict = {}
n, k = [int(x) for x in input().split()]
for _ in range(n):
    tmp = input().split()
    my_dict[tmp[0]] = int(tmp[1])

my_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
for key in my_dict.keys():
    if k > 0:
        print(key, end=' ')
        k -= 1
    else:
        break
''' 
Hung 6
Long 7
Giang 8
Linh 5
Tuan 8
Hoa 9
Mai 5
Ngoc 4
Khanh 9
Ngan 10
'''