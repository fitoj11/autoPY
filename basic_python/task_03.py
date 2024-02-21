from math import log, sqrt, sin, pi, cos, tan, asin, acos, degrees
import math
# v=float(input())
# if v <= 0:
#     print('error')
# elif v <= 7.8:
#     print('0')
# elif v < 11.2:
#     print('1')
# elif v <= 16.4:
#     print('2')
# else:
#     print('3')

# a=float(input())
# h=float(input())
# v=(a**2*h)/(4*sqrt(3))
# s=((a**2*sqrt(3))/4)+(((3*a)/2)*sqrt(h**2+(a**2/12)))
# print(round(v, 3), round(s, 3))

# year=int(input())
# if year < 0:
#     print('error')
# else:
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 != 0:
#             print(365)
#         else:
#             print(366)
#     else:
#         print(365)

# k=int(input())
# if k < 0 or k > 99:
#     print('ошибка')
# else:
#     if k % 2 != 0:
#         print(k, 'рублей')
#     else:
#         print(k, 'рубля')
# import math
# a=float(input())
# b=float(input())
# v=int(input())
# if a > 0 and b > 0 and v > 0:
#     quantity=((5*a**2)*(b/1000))/v
#     if quantity <= 0 or a <= 0 or b <= 0 or v <= 0:
#         print('error')
#     else:
#         print(math.ceil(quantity))
# else:
#     print('error')

h=int(input())
m=int(input())
s=int(input())
if h >= 0 and h < 12 and m >= 0 and m < 60 and s >= 0 and s < 60:
    angle = h * 30 + m * 0.5 + s / 120
    print(round(angle, 2))
else:
    print('error')


