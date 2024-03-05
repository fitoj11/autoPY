import numpy as np
import numpy.linalg as alg

array_list = [ ]
for i in range(2):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
a = np.array(array_list, dtype=float)
n = float(input())
# print(a, n)
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
a_02 = np.polyfit(a[0], a[1], 2)
# print(a_02)
ok = get_trend(n, a_02)
# print(ok)
print("Дальность: %6.2f м" % ok)