import matplotlib.pyplot as plt
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
x_trend = [i for i in range(0,1500,10)]
y_trend = [get_trend(x, a) for x in x_trend]
plt.plot(x_array, h_array, 'go', label="положение снаряда")
plt.plot(x_trend, y_trend, 'r-', label="линия тренда")
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.legend(loc="lower center")
plt.show()