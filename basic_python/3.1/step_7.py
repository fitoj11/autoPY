import numpy as np

path = input()
path = path.split()
path = np.array(path, dtype = float)
speed = input()
speed = speed.split()
speed = np.array(speed, dtype = float)
k = int(input())
p = int(input())
len_path = path[k:p+1].sum()
t_path = sum(path[k:p+1] / speed[k:p+1])
avg_speed = len_path / t_path
print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (len_path, t_path, avg_speed))