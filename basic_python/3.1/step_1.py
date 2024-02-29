import numpy as np

line = input("Введите числа через пробел : ")
list_a = line.split()
a = np.array(list_a, dtype=int)
print("a = ", a)
print("Сумма = ", a.sum())
print("Произведение = ", a.prod())
print("Среднее = ", a.mean())
print("Максимум = ", a.max())
print("Минимум = ", a.min())
