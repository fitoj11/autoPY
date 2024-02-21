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

def vklad():
    for x in range(1000, 35000):
        k = 5
        n = 13
        s = x*((1+(k/(12*100)))**n)
        vklad_prib = s - x
        if round(vklad_prib, 1) == 1859.0:
            return x
print(round(vklad()))