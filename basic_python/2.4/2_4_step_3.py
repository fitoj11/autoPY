ox = input()
ox_list = ox.split()
ox_list = [float(x) for x in ox_list]
n = int(input())
a = float(input())
b = float(input())
for_year = 0
for i in range(len(ox_list)):
    if ox_list[i] >= n:
        dif = ox_list[i] - n
        for_year = for_year + (dif * b)
        for_year = for_year + abs((ox_list[i] - dif) * a)
    else:
        for_year = for_year + (ox_list[i] * a)
sum_for_year = sum(ox_list)
print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (sum_for_year, for_year))