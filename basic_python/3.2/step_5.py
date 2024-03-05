import numpy as np

x_array = input()
x_array = x_array.split()
x_array = np.array(x_array, dtype = float)
h_array = input()
h_array = h_array.split()
h_array = np.array(h_array, dtype = float)
a_01 = np.polyfit(x_array, h_array, 1)
a_02 = np.polyfit(x_array, h_array, 2)
def get_trend_one(x, a):
    y = a[0] * x + a[1]
    return y
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
one_y = sum(get_trend_one(x_array, a_01)) / len(x_array)
two_y = sum(get_trend(x_array, a_02)) / len(x_array)
x0 = sum(get_trend_one(x_array, a_01))
xt = sum(x_array)
x01 = sum(get_trend(x_array, a_02))
avg_01 = ((get_trend_one(x_array, a_01) - h_array) / get_trend_one(x_array, a_01)) * 100
avg_02 = ((get_trend(x_array, a_02) - h_array) / get_trend(x_array, a_02)) * 100
# print(avg_01, avg_02)
if abs(sum(abs(avg_01)) / len(x_array)) > abs(sum(abs(avg_02)) / len(x_array)):
    print("%5.3f %5.3f %5.3f" % (a_02[0], a_02[1], a_02[2]))
else:
    print("%5.3f %5.3f" % (a_01[0], a_01[1]))
# print(abs(round(one, 3)))
# print(abs(one_y))
# # print(abs(round(two, 3)))
# print(abs(two_y))
# print(a_01)
# print(a_02)
# delta_h = abs(h_array - one)
# print(delta_h)
# k_poly = np.polyfit(month, temperature, 2)
# print(k_poly)
# delta = np.abs((temperature - get_trend(month, k_poly)) / temperature) * 100
# print("погрешность:", np.round(delta, 1))