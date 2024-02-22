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
step_2(300000, 6, 20)
# f = open("имя файла", "режим открытия", "кодировка" )


