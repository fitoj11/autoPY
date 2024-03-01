import numpy as np

a = np.array([5, 5, 2, 6, -1])
b = np.array([2, 7, 2, 3, -1])
print(np.where(a == b)[0])
print(np.where(a > b)[0])
print(np.where(a < 3)[0])
print(np.where(b > 10)[0])
print(np.where(a >= b.mean())[0])
print(np.where(a + b >= 8)[0])
print(np.where(np.logical_and(a > 0, a <= 6)))
print(np.where(np.logical_or(
    np.logical_and(a > 0, a < 6),
    np.logical_or(b < 0, b > 7)
)))
a = np.array([5, 5, 1, 6, 15, 3, 8, -1])
print(a[2:6])
print(a[1:6:2])

a = np.array([2, 5, 2, 0, 0])
b = np.array([5, -1, -1, 6, 2])
c = np.where(a == b)[0]
print(c)