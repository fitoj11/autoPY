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
def vklad():
    x = float(input())
    k = float(input())
    n = float(input())
    s = x*((1+(k/(12*100)))**n)
    vklad_prib = s - x
    return vklad_prib
print(round(vklad()))