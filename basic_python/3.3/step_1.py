import numpy.linalg as alg
import numpy as np

a = np.array([[3, 4, -1], [-2, 1, 3]])
b = np.array([[1, 0, -5], [2, 2, -1]])
c = a + b
print("a:\n", a)
print("b:\n", b)
print("c:\n", c)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 1], [2, 3]])
c = np.dot(a, b)
print("a:\n", a)
print("b:\n", b)
print("c:\n", c)

a = np.array([[1, 2, 3], [0, 1, -3], [2, 1, 4]])
det_a = alg.det(a)
print("a:\n", a)
print("определитель = ", det_a)

a = np.array([[1, 2, 3], [0, 1, -3], [2, 1, 4]])
inv_a = alg.inv(a)
print("a:\n", a)
print("inv_a:\n", inv_a)