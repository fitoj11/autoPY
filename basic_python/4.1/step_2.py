import numpy as np

a = input()
a = a.split()
a = np.array(a, dtype = float)
# print(a)
# print(len(a))
for i in range(len(a)):
    b = a[i] / 60
    if b >= 12:
        print(i)