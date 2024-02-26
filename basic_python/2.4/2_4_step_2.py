from math import log, sqrt, sin, pi, cos, tan, asin, acos, degrees, atan
ox = input()
ox_list = ox.split()
ox_list = [float(x) for x in ox_list]
oy = input()
oy_list = oy.split()
oy_list = [float(x) for x in oy_list]
k = int(input())
r = float(input())
# print(ox_list, oy_list, k, r)

# for i in range(len(ox_list)): # отладка
#     distances = sqrt((ox_list[i]-0)**2+(oy_list[i]-0)**2)
#     if i == k:
#         k_dist = distances
#     print(distances)
# print(k_dist)
count = 0
for i in range(len(ox_list)):
    distances = sqrt((ox_list[i]-ox_list[k])**2+(oy_list[i]-oy_list[k])**2)
    if distances <= r:
        count = count + 1
print(count)

# count = 0
# for d in distances:
#     if # сравните расстояние d с радиусом действия r
#         count = count +1