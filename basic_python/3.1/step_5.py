import numpy as np

costs = np.array([1200, 1300, 900, 1450, 1300, 1000, 900, 1000, 1450, 1450, 1300, 1400])
sum_winter = np.sum(costs[0:2]) + np.sum(costs[11])
sum_summer = np.sum(costs[5:8])
if sum_winter > sum_summer:
    print("Зимой на проезд потрачено больше денег, сумма: %4d руб." % sum_winter)
elif sum_winter < sum_summer:
    print("Летом на проезд потрачено больше денег, сумма: %4d руб." % sum_summer)
else:
    print("Зимой и летом на проезд тратится одинаковая, сумма: %4d руб." % sum_winter)
max_costs = np.max(costs)
max_month = np.where(costs==max_costs)[0][0:11]
print("Самая большая сумма:%4d руб., потрачена в следующих месяцах:" % max_costs, max_month + 1)