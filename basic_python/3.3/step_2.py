import numpy as np
import numpy.linalg as alg

a = np.array([[3, 4, -2], [-2, -1, 4], [1, 2, 1]])
print("A :\n", a)
b = np.array([[1, -3, -2, 1], [2, 4, -2, -1], [5, -2, 0, -2]])
print("B :\n", b)
c = np.dot(a, b)
print("A*B:\n", c)
det_a = alg.det(a)
print("dеt(A): ", round(det_a, 1))
a_inv = alg.inv(a)
print("A^-1:\n", np.round(a_inv,1))
a_3 = np.dot(a, np.dot(a,a))
result = det_a * np.dot(a_inv, b) - 10 * np.dot(a_3, b)
print("Result:\n", result)