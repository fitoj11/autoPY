# print("123")
#
# name = str(input('What your name '))
# print("name is " + name)

# x = 5
# y = 3
# print(x + y ** 2)
# print(y ** 2 * x)
# print(x ** y - x)
# print(x ** (y - 2))
# print(x / y + 3)
# print(x / y * 3)
# print(x // y)
# print(x % y)
# print(x == y or (x - 4) >= 1)
# print(x != 2 and y <= 5)

# print(
# round(3.89),
# round(-2.49),
# round(4.999,2),
# abs(-5),
# abs(6.1),
# min(3, -2, -3.1, 0.2),
# max(1.9, -2, -3.1, 0.2),
# abs(min(3, -2, -3.1, 0.2)),
# min(3, abs(-2), abs(-3.1), 0.2))

def popular(bmi, x, y, a):
    if bmi < x:
        description = "недостаточной массой тела."
    elif bmi < y:
        description = "нормальной массой тела."
    elif bmi < a:
        description = "избыточной массой тела."
    else:
        description = "ожирением."
    text = print("Ваш индекс массы тела:", bmi, "Вы относитесь к группе людей с", description)
    return text

name = str(input("Whats your name? "))
age = int(input("Сколько Вам полных лет? "))
height = float(input("Ваш рост? "))
weight = float(input("Ваш вес? "))
bmi = weight / height ** 2
bmi = round(bmi, 2)
if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")
else:
    if age < 45:
        popular(bmi, 18.5, 25, 30)
    else:
        popular(bmi, 22, 27, 32)