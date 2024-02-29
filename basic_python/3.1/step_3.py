import numpy as np

path = input()
path = path.split()
path = np.array(path, dtype = float)
speed = input()
speed = speed.split()
speed = np.array(speed, dtype = float)
len_path = path.sum()
# print("Расстояние между пунктами А и В :", len_path)
len_path = np.sum(path)
time = path / speed
# print("Время на каждом участке :", np.round(time, 2))
sum_time = time.sum()
avg_speed = len_path / sum_time
print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, sum_time, avg_speed))