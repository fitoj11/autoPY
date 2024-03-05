import numpy as np
import numpy.linalg as alg

array_list = [ ]
for i in range(2):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
a = np.array(array_list, dtype=float)
# print(a)
tax = a[1] / a[0]
# print(tax)
s = sum(a[0])
p = 0
for i in range(len(a[0])):
    if tax[i] > 0 and tax[i] <= 30:
        p = p + 1
    elif tax[i] <= 60:
        p = p + 1.5
    elif tax[i] <= 120:
        p = p + 3
    elif tax[i] > 120:
        p = p + 4.5
    else:
        print('error')
print("Длина пути: %3d км, оплата: %5.2f S$"  % (s, p))
