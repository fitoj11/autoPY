import matplotlib.pyplot as plt
from math import log, sqrt, sin, pi, cos, tan, asin, acos, degrees, atan, e, radians, pow, exp, degrees

# plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25 ])
# plt.show()

# import matplotlib.pyplot as plt
# # формируем линию
# line = plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25 ])
# # задаем формат ее вывода
# plt.setp(line, color="red", linewidth=2, marker="o" )
# # устанавливаем две оси в положение zero
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# # скрываем остальные две
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# # отображаем область построения
# plt.show()

import matplotlib.pyplot as plt
# from task_04 import f_x
# def f_x(x):
#    y = x ** 3 - 6 * x ** 2 +  x + 5
#    return y
# a = -2
# b = 6
# n = 100
# h = (b-a)/(n-1)
# x_list = [a + h * i for i in range(n)]
# f_list = [f_x(x) for x in x_list]
# line = plt.plot(x_list, f_list)
# plt.setp(line, color="blue", linewidth=2)
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# plt.show()

# import matplotlib.pyplot as plt
# from task_04 import n_t
# years = [x for x in range(1500, 2000)]
# f_list = [n_t(t_main) for t_main in years]
# x_list = years
# line = plt.plot(x_list, f_list)
# plt.setp(line, color="blue", linewidth=2)
# plt.gca().spines["left"].set_position("center")
# plt.gca().spines["bottom"].set_position("center")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# plt.grid()
# plt.show()

def f_x(x):
    y = ((exp(cos((x))))+(log(((pow(sin(0.8*(x)),2))+1))*(cos((x)))))
    return y
def y_x(x):
    y = -log((pow(cos((x))+sin((x)), 2))+1.7)+2
    return y
a = -2
b = 6
n = 100
h = (b-a)/(n-1)
x_list = [a + h * i for i in range(n)]
f_list = [f_x(x) for x in x_list]
y_list = [y_x(x) for x in x_list]
line_f = plt.plot(x_list, f_list, label='f(x)')
line_y = plt.plot(x_list, y_list, label='y(x)')
plt.setp(line_f, color="blue", linewidth=2)
plt.setp(line_y, color="red", linewidth=2)
plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.legend()
plt.title("Графики функций")
plt.show()