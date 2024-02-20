from math import log, sqrt, sin, pi, cos, tan, asin, pi

x = float(input())
y = float(input())
first = asin(cos(x+sqrt(3)/2*pi))
second = 1.2*sqrt(2-cos(y)**2)
three = x**2+y**2+1
z = (first + second) / three
print(round(z, 5))

