import numpy as np
import numpy.linalg as alg

a = np.array([[1, -3, -2, 1], [2, 4, 3, -1], [5, -2, 0, -2], [1, 4, 1, -1]])
print("A :\n", a)
det_bl = alg.det(a[:2,1:3])
print("det(block) = ", det_bl)
sum_diag = np.sum(np.diag(a))
print("sum_diag =  ", sum_diag)
max_col = np.max(a, 0)
print("max_col :", max_col)
min_row = np.min(a, 1)
print("min_row :", min_row)