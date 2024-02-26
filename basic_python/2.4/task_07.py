temp_0 = input()
temp_0_list = temp_0.split()
x0_list = [float(x) for x in temp_0_list]
temp_12 = input()
temp_12_list = temp_12.split()
x12_list = [float(x) for x in temp_12_list]
avg_temp = float(input())
for i in range(len(x0_list)):
    avg_temp_tek = (x0_list[i] + x12_list[i]) / 2
    if avg_temp_tek > avg_temp:
        print(i)