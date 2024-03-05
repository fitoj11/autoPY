import numpy as np
import numpy.linalg as alg

array_list = [ ]
for i in range(2):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
c = np.array(array_list, dtype=float)
# print(c)
a = c[0]
h = c[1]
v_max = 0
s_min = 0
list_v = []
list_s = []
i = 0
while i < len(c[0]):
    v = a[i] ** 2 * h[i] / 3
    s = 2 * a[i] * np.sqrt(0.25 * a[i] ** 2 + h[i] ** 2)
    list_v.append(v)
    list_s.append(s)
    i+=1
# print(list_v.index(max(list_v)))
# print(max(list_v), min(list_s))
print("Vmax: %2d, %8.2f, Smin: %2d, %8.2f" % (list_v.index(max(list_v)), max(list_v), list_s.index(min(list_s)), min(list_s)))
#
# for i in range(len(c[0])):
#     v = a[i]**2 * h[i]/3
#     if v_max < v:
#         v_max = v
# for i in range(len(c[0])):
#     s = 2 * a[i] * np.sqrt(0.25*a[i]**2 + h[i]**2)
#     print(s)
#     if s_min > s:
#         s_min = s
#     else:
#         s_min = s_min
# print(v_max, s_min)
#
# a=list(map(float,input().split()))
# b=list(map(float,input().split()))
# list_v=[]
# list_s=[]
# count=0
# while count<len(a):
#     h=(b[count]*b[count]+(a[count]/2)**2)**0.5
#     s=2*a[count]*h
#     v=((a[count]**2*b[count])/3)
#     list_v.append(v)
#     list_s.append(s)
#     count+=1
# print(f'Vmax: {list_v.index(max(list_v))}, {round(max(list_v),2)}, Smin: {list_s.index(min(list_s))}, {round(min(list_s),2)}')