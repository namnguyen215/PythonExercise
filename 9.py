# KHOANG CACH HAVERSINE
import math

long1, lat1 = [float(x) for x in input().split()]
long2, lat2 = [float(x) for x in input().split()]

deltaLat, deltaLong = lat2 - lat1, long2 - long1
sinLat = math.sin(deltaLat/2)
sinLong = math.sin(deltaLong/2)
a = sinLat * sinLat + math.cos(lat1) * math.cos(lat2) * sinLong * sinLong
c = 2 * math.asin(math.sqrt(a))
d = 6371 * c
print(f"{d:.2f}")

'''
105.96 10.21
107.17 16.79
'''
