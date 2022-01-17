lst=[9,8,20,3,4,-1,0]
max1=max2=max3=-(10^9)
for x in lst:
    if(x>max1):
        max1=x
for x in lst:
    if(x>max2 and x<max1):
        max2=x
for x in lst:
    if(x<max1 and x<max2 and x>max3):
        max3=x
print(max1+max2+max3)