import math
# def f_x(x):
#    try:
#        y = 1 / (x+1) + x / (x-3)
#    except:
#        y = math.inf
#    return y
# t = float(input("t = "))
# y = f_x(t)
# print("f(", t, ") = ", y)

# def vklad():
#     x = float(input())
#     k = float(input())
#     n = float(input())
#     s = x*((1+(k/(12*100)))**n)
#     vklad_prib = s - x
#     return vklad_prib
# print(round(vklad()))

# x_list = [-6, -7, -8, -9, -10]
# for i in range(len(x_list)):
#     print("x_list[%1d] = %5.2f" % (i, x_list[i]))
# print(*list(range(0, 9, 2)))
# print(*list(range(-6, -11, -1)))
# print(*list(range(3, 13, 3)))
# print(*list(range(0, 6)))

# def vklad():
#     for x in range(1000, 35000):
#         k = 5
#         n = 13
#         s = x*((1+(k/(12*100)))**n)
#         vklad_prib = s - x
#         if round(vklad_prib, 1) == 1859.0:
#             return x
# print(round(vklad()))
#
# x_list = [i / (i + 1) for i in range(4)]
# print(list(x_list))
# y_list = [x + 2 for x in x_list] # испльзование списка x_list, преобразование его элементам от X, выражение X+2
# print(list(y_list))

import math
def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y
a = float(input("a = "))
b = float(input("b = "))
n = int(input("n = "))
if n < 0 or a >= b:
    print("Ошибочные входные данные")
else:
    h = (b - a) / (n - 1)
    x_list = [a + i * h for i in range(n)]
    f_list = [f_x(x) for x in x_list]
    print("-" * 17)
    print(f'| {"x":^6s} | {"f(x)": ^5s} |')
    print("-" * 17)
    for i in range(n):
        print(f'| {x_list[i]:6.3f} | {f_list[i]:5.3f} |')
    print("-" * 17)

        # s = input(("x_list = "))
# str_list = s.split()
# x_list = [float(x) for x in str_list]
# for x in x_list:
#     y = f_x(x)
#     print("f(%4.2f) = %6.3f" % (x,  y))
