import numpy as np
import numpy.linalg as alg

k = float(input())
p = float(input())
s = float(input())
if k > 0 and p > 0 and s > 0:
    summ = (12/100) * s * p * 2
    sam = k * 3
    otvet = min(summ, sam)
    print(round(otvet, 2))
else:
    print('error')
# print(summ, sam)