import numpy as np
import numpy.linalg as alg

a = [[1, 1, 1], [-1/3, 1, 0], [0, -1/3, 1]]
b = [2970, 180, 130]
det_a = alg.det(a)
a_inv = alg.inv(a)
x = np.dot(a_inv, b)
# print(a)
# print(b)
print("%4.0f р., %4.0f р., %4.0f р." % (x[0], x[1], x[2]))