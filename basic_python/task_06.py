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

f = open("lambda_exp.txt", "r")
t_list =[]
lambda_exp_list = []
for line in f:
    t_lambda_list = line.split()
    t_list.append(float(t_lambda_list [0]))
    lambda_exp_list.append(float(t_lambda_list [1]))
f.close()
lambda_list =[compute_lambda(t) for t in t_list]
error_list = [abs((lambda_exp_list[i] - lambda_list[i]) / lambda_exp_list[i] )
              for i in range(len(t_list))]
print("-" * 40)
print("|%7s | %7s | %7s |%8s |" % ("t","l(t)","exp(t)", "error"))
print( "-" * 40)
for i in range(len(t_list)):
    print("|%7d | %7.3f | %7.1f |%7.2f%% |"
          % (t_list[i], lambda_list[i], lambda_exp_list[i], error_list[i] * 100))
print("-" * 40)
max_error = max(error_list)
index_max_error = error_list.index(max_error)
print("Максимальная погрешность = %5.2f%%  при t = %5d"
      % (max_error * 100, t_list[index_max_error]))
min_error = min(error_list)
index_min_error = error_list.index(min_error)
print("Минимальная погрешность = %5.2f%%  при t = %5d"
      % (min_error * 100, t_list[index_min_error]))
avg_error = sum(error_list) / len(t_list)
print("Средняя погрешность = %5.2f%%" % (avg_error * 100))