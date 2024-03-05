import numpy as np
import numpy.linalg as alg

n = int(input())
array_list = [ ]
for i in range(n):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
a = np.array(array_list, dtype=float)
avg_x = np.mean(a, 0)
# print(a)
# print(avg_x)
longmax = 0
for x in range(n):
    l = a[x]
    long = np.sqrt((l[0]-avg_x[0])**2 + (l[1]-avg_x[1])**2)
    # long = np.sqrt((avg_x[0] - l[0]) ** 2 + (avg_x[1] - l[1]) ** 2)
    if longmax <= long:
        longmax = long
# print(longmax)
print("центр в точке (%6.3f, %6.3f), r = %6.3f" % (avg_x[0], avg_x[1], longmax))