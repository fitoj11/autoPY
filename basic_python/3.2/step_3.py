import numpy as np

x_array = input()
x_array = x_array.split()
x_array = np.array(x_array, dtype = float)
h_array = input()
h_array = h_array.split()
h_array = np.array(h_array, dtype = float)
k = float(input())
p = float(input())
a = np.polyfit(x_array, h_array, 2)
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y
h_zero = get_trend(0, a)
h_target = get_trend(k, a)
delta_h = abs(p - h_target)
if delta_h <= 0.5:
    popal = 'yes'
else:
    popal = 'no'
print("h0 = %6.2f, %2s" % (h_zero, popal))