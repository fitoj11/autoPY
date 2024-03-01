import  numpy as np
def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y
month = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
temperature = np.array([4, 8, 14, 19, 23, 27, 29, 28, 25, 18, 11, 6])
k_poly = np.polyfit(month, temperature, 2)
print(k_poly)
delta = np.abs((temperature - get_trend(month, k_poly)) / temperature) * 100
print("погрешность:", np.round(delta, 1))