from math import log, sqrt, sin, pi, cos, tan, asin, acos, degrees
#
# x = float(input())
# y = float(input())
# first = asin(cos(x+sqrt(3)/2*pi))
# second = 1.2*sqrt(2-cos(y)**2)
# three = x**2+y**2+1
# z = (first + second) / three
# print(round(z, 5))
#
# def compute_len(x_0, y_0, x_1, y_1):
#     len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
#     return len_line
# c = compute_len(x_a, y_a, x_b, y_b)
# a = compute_len(x_b, y_b, x_c, y_c)
# b = compute_len(x_a, y_a, x_c, y_c)
#
# def compute_resist(r_1, r_2):
#    r = r_1 * r_2 / (r_1 + r_2)
#    return r
# res = compute_resist(12.0, 12.0)

def compute_len(x_0, y_0, x_1, y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line
def compute_area(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area
def compute_angle(a_1, a_2, a_3):
    angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2) /
                     (2 * a_1 * a_2))
    return degrees(angle_rad)
def vpis(a, b, c, p):
    r_vpis = sqrt((p/2-a)*(p/2-b)*(p/2-c)/(p/2))
    return r_vpis
def vokryg(a, b, c, s):
    r_vokryg = (a*b*c)/(4*s)
    return r_vokryg
def median(a, b, c):
    med_a = (1/2)*sqrt(2*(c**2+b**2)-a**2)
    med_b = (1/2)*sqrt(2*(a**2+c**2)-b**2)
    med_c = (1/2)*sqrt(2*(a**2+b**2)-c**2)
    sum_med = med_a + med_b + med_c
    return sum_med
x_a = float(input())
y_a = float(input())
x_b = float(input())
y_b = float(input())
x_c = float(input())
y_c = float(input())
c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)
if a + b <= c or b + c <= a or a + c <= b:
    print("error")
else:
    s = compute_area(a, b, c)
    p = a + b + c
    rad = vpis(a, b, c, p)
    radop = vokryg(a, b, c, s)
    sum_med = median(a, b, c)
    print(round(rad, 4), round(radop, 4), round(sum_med, 4))

# print("Стороны : ", round(a, 3), round(b, 3), round(c, 3))
# print("Площадь : ", round(s, 3))
# print("Периметр : ", round(p, 3))
# print("Углы : ", round(angle_A, 3), round(angle_B, 3), round(angle_C, 3))