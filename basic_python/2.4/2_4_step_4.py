s = int(input())
n = int(input())
k = int(input())
k_a = k/(12*100)
p_k = ((k_a * (1+k_a)**n) / (((1+k_a)**n) - 1)) * s
dev_k_a = (p_k*n) - s
dev_p = s
for i in range(n):
    p = s/n + ((s-((i)*s/n)) * k/(12*100))
    dev_p = dev_p - p
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (i+1, p, p_k))
print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (abs(dev_p), dev_k_a))
# print(p, k, p_k)