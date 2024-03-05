import numpy as np
import numpy.linalg as alg

array_list = [ ]
for i in range(2):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
a = np.array(array_list, dtype=float)
# print(a)
b = np.sum(np.reciprocal(a[0]))
c = 1/b
# print(c)
i = np.sum(a[1])
# print(i)
u = i * c
# print(u)
print("R = %6.3f Ом, I = %6.3f А, U = %6.3f В" % (c, i, u))