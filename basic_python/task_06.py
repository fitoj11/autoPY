def compute_lambda(t):
    b = 33
    l_0 = 884
    t_0 = 100
    return (b * l_0 /(t-t_0))
def p_t(t, s, n, k):
    return (s/n+(s-(t-1)*(s/n))*k/(12*100))
def step_2(s, n, k):
    if s <= 0 or n <= 0 or k <= 0:
        print("error")
    else:
        t_list = [i + 1 for i in range(0,n)]
        lambda_list = [p_t(t, s, n, k) for t in t_list]
        bank_profit = 0
        for i in range(0,n):
            print("%2d месяц - %8.2f руб" % (t_list[i], lambda_list[i]))
            bank_profit = bank_profit + lambda_list[i-1]
        print("Доход банка - %6.2f руб" % (bank_profit-s))
# step_2(int(input()), int(input()), int(input()))

# f = open("student.txt", "r", encoding = "utf-8-sig")
# for student in f:
#    print("Информация о студенте : ", student)
# for student in f:
#     student_list = student.split()
#     print("Информация о студенте в виде списка: ", student_list)
#список для фамилий
# list_second_name = []
# #список оценок по первой дисциплине
# list_mark_1 =[]
# for student in f:
#     student_list = student.split()
#     # заносим оценки в соответствующие переменные,
#     # преобразуя их к целому типу
#     mark_1 = int(student_list[1])
#     mark_2 = int(student_list[2])
#     mark_3 = int(student_list[3])
#     # вычисляем среднюю оценку
#     avg_mark = (mark_1 + mark_2 + mark_3) / 3
#     print(student_list[0], ", средняя оценка : ", avg_mark)
#     # добавляем очередную фамилию к списку
#     list_second_name.append(student_list[0])
#     # добавляем очередную оценку к списку
#     list_mark_1.append(mark_1)
# print("Список фамилий : ", list_second_name)
# print("Список оценок по первой дисциплине : ", list_mark_1)
# print("Средний балл по первой дисциплине : ", sum(list_mark_1)/len(list_mark_1))
# f.close()
#
# f = open("students.txt","a", encoding="utf-8-sig")
# f.write("Федоров 5 5 5\n")
# f.write("Яковлев 5 5 5\n")
# f.close()

# f = open("students.txt", "r")
# number_list = []
# number_list.append(1234)
# number = float(1234)
#
# # for line in f:
# #     number = float(line)
# #     number_list.append(number)
# sum_number = sum(number_list)
# print("sum = ", sum_number)
# f.close()

from math import log, sqrt, sin, pi, cos, tan, asin, acos, degrees, atan
import math
def n_t(t_main):
    try:
        c = 172
        t = 45
        t1 = 2000
        y = (c/t)*((pi/2)-atan((t1-t_main)/t))
    except:
        y = math.inf
    return y
s = [1000, 1750, 1800, 1850, 1900, 1950, 1955,
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995,
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]
t_list = s
x_list = [int(t_main) for t_main in t_list]
for t_main in x_list:
    y = n_t(t_main)
    # print("%6.3f" % (y))
    y_list = [n_t(t_main) for t_main in x_list] # массив с расчетами по формуле
# y_list = [int(t_main) for t_main in t_list]
# print(y_list)
population =[0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
             2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
             5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
             7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]
# f = open("lambda_exp.txt", "r")
# t_list =[]
# lambda_exp_list = []
# for line in f:
#     t_lambda_list = line.split()
#     t_list.append(float(t_lambda_list [0]))
#     lambda_exp_list.append(float(t_lambda_list [1]))
# f.close()
# # t_list = t_list[1:13]
# lambda_list =[compute_lambda(t) for t in t_list]
error_list = [abs((population[i] - y_list[i]) / population[i])
              for i in range(len(t_list))]
# print("-" * 40)
# print("|%7s | %7s | %7s |%8s |" % ("t","l(t)","exp(t)", "error"))
# print( "-" * 40)
for i in range(len(t_list)):
    y = n_t(i)
#     print("|%7d | %7.3f | %7.3f |%7.2f%% |"
#           % (t_list[i], y_list[i], population[i], error_list[i] * 100))
# print("-" * 40)

first = int(input())
second = int(input()) + 1

max_error = max(error_list[first:second])
index_max_error = error_list.index(max_error)
# print("Максимальная погрешность = %5.2f%%  при t = %5d"
#       % (max_error * 100, t_list[index_max_error]))
min_error = min(error_list[first:second])
index_min_error = error_list.index(min_error)
# print("Минимальная погрешность = %5.2f%%  при t = %5d"
#       % (min_error * 100, t_list[index_min_error]))
avg_error = sum(error_list[first:second]) / len(t_list[first:second])
# print("Средняя погрешность = %5.2f%%" % (avg_error * 100))
print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f"
      % (t_list[index_min_error], t_list[index_max_error], avg_error * 100))
#
# import matplotlib.pyplot as plt
# line_th = plt.plot(t_list, lambda_list, label = 'теоретические')
# line_exp = plt.plot(t_list, s, label = 'экспериментальные')
# # задаем стили для линий
# plt.setp(line_exp, color= "blue", linestyle = "--", linewidth = 2 )
# plt.setp(line_th, color= "red", linewidth = 2)
# plt.legend()
# plt.gca().spines["left"].set_position("zero")
# plt.gca().spines["bottom"].set_position("zero")
# plt.gca().spines["top"].set_visible(False)
# plt.gca().spines["right"].set_visible(False)
# plt.title("Значения теплопроводности")
# plt.show()