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

# def f_x(x):
#     y = exp(cos(x)) + log(pow(sin(0.8*x), 2) + 1) * cos(x)
#     return y
# def y_x(x):
#     y = -log((pow(cos((x))+sin((x)), 2))+1.7)+2
#     return y
# a = -240
# b = 360
# n = 100
# h = (b-a)/(n-1)
# x_list = [a + h * i for i in range(n)]
# f_list = [f_x(x) for x in x_list]
# y_list = [y_x(x) for x in x_list]
# line_f = plt.plot(x_list, f_list, label='f(x)')
# line_y = plt.plot(x_list, y_list, label='y(x)')
# plt.setp(line_f, color="blue", linewidth=2)
# plt.setp(line_y, color="red", linewidth=2)
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# plt.legend()
# plt.title("Графики функций")
# plt.show()

# from matplotlib.patches import  Circle
# import matplotlib.pyplot as plt
# plt.xlim(0, 12)
# plt.ylim(0, 12)
# ax = plt.gca()
# circle = Circle((6, 7),5)
# ax.add_patch(circle)
# plt.show()

# from matplotlib.patches import Path, PathPatch
# import matplotlib.pyplot as plt
# n = 8
# m  = 8
# plt.xlim(0, n)
# plt.ylim(0, m)
# ax = plt.gca()
# vertices = [(0, 6), (2, 8), (2, 4), (4, 6), (4, 2), (6,4), (6, 0), (8,2)]
# codes = [1, 2, 1, 2, 1, 2, 1, 2]
# path = Path(vertices, codes)
# path_patch = PathPatch(path, lw=3)
# ax.add_patch(path_patch)
# ax.axes.set_axis_off()
# plt.show()

from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch
import matplotlib.pyplot as plt
# def draw_cat(ax):
#     # туловище
#     poly = [(3, 1), (4, 14), (5, 11), (8, 11), (9, 14), (10, 1)]
#     polygon = Polygon(poly, fc="grey", ec="black", lw=4)
#     ax.add_patch(polygon)
#     # глаза
#     circle = Circle((5.3, 8.5), 1.2, fc="white", ec="black", lw=4)
#     ax.add_patch(circle)
#     circle = Circle((7.7, 8.5), 1.2, fc="white", ec="black", lw=4)
#     ax.add_patch(circle)
#     # зрачки
#     circle = Circle((6, 8.3), 0.1, fc="black", ec="black", lw=4)
#     ax.add_patch(circle)
#     circle = Circle((7, 8.3), 0.1, fc="black", ec="black", lw=4)
#     ax.add_patch(circle)
#     # нос
#     circle = Circle((6.5, 7.5), 0.3, fc="black", ec="black", lw=4)
#     ax.add_patch(circle)
#     # задние лапы
#     wedge = Wedge((3, 1), 2, 86, 180, fc="grey", ec="black", lw=4)
#     ax.add_patch(wedge)
#     wedge = Wedge((10, 1), 2, 0, 94, fc="grey", ec="black", lw=4)
#     ax.add_patch(wedge)
#     # передние лапы
#     ellipse = Ellipse((5.5, 1.2), 2, 1.5, fc="grey", ec="black", lw=4)
#     ax.add_patch(ellipse)
#     ellipse = Ellipse((7.5, 1.2), 2, 1.5, fc="grey", ec="black", lw=4)
#     ax.add_patch(ellipse)
#     # улыбка
#     arc = Arc((6.5, 6.5), 5, 3, angle=0, theta1=200, theta2=340, lw=4, fill=False)
#     ax.add_patch(arc)
#     # линия между носом и улыбкой, усы
#     vertices = [(6.5, 5), (6.5, 7.5), (10, 6), (6.5, 7.5), (10, 6.5), (6.5, 7.5), (10, 7),
#                 (6.5, 7.5), (3, 6), (6.5, 7.5), (3, 6.5), (6.5, 7.5), (3, 7)]
#     # число 1 соответствует команде matplotlib.path.Path.MOVETO
#     # число 2 соответствует команде matplotlib.path.Path.LINETO
#     codes = [1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
#     path = Path(vertices, codes)
#     path_patch = PathPatch(path, fill=False, lw=1)
#     ax.add_patch(path_patch)
# n = 13
# m  = 15
# plt.xlim(0, n)
# plt.ylim(0, m)
# ax = plt.gca()
# draw_cat(ax)
# ax.axes.set_axis_off()
# plt.show()

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Ellipse, Rectangle, Wedge
n = 20
m = 20
fig, ax = plt.subplots()
# Создание и добавление каждой фигуры на график
# arc = Arc((6, 6), 5, 3, angle=0, theta1=200, theta2=100)
# ellipse = Ellipse((5, 1), 2, 3)
# rectangle = Rectangle((10, 12), 5, 8)
# wedge = Wedge((4, 4), 2, -90, 90)

figure = Ellipse(5, 1, 2, 3)
# figure = Arc((6, 6), 5, 3, 0, 200, 100)
# figure = Ellipse((5, 1), 2, 3)
# figure = Circle((6, 7), 5, 1)
# figure = Rectangle((10, 12), 5, 8)
# ax.add_patch(arc)
# ax.add_patch(ellipse)
# ax.add_patch(rectangle)
ax.add_patch(figure)
plt.xlim(0, n)
plt.ylim(0, m)
ax = plt.gca()
plt.show()