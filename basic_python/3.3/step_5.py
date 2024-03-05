import numpy as np
import numpy.linalg as alg
import math as mp

ver = int(input())
array_list = [ ]
for i in range(ver):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
a = np.array(array_list, dtype=int)
grad = int(input())
# print(ver, a, grad)
rotate = [[np.cos(mp.radians(grad)), np.sin(mp.radians(grad))], [-np.sin(mp.radians(grad)), np.cos(mp.radians(grad))]]
# print(rotate)
mass = np.dot(a, rotate)
# print(mass)
avg_x = np.mean(mass, 0)
# print(avg_x)
print("avg_x = %6.2f, avg_y = %6.2f" % (avg_x[0], avg_x[1]))