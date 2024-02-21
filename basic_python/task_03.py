from math import log, sqrt, sin, pi, cos, tan, asin, acos, degrees
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

year=int(input())
if year < 0:
    print('error')
else:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print(365)
        else:
            print(366)
    else:
        print(365)