import numpy as np

H = int(input())
T = int(input())
t = float(input())
h=(H/2*(1-np.cos(2*np.pi*t/T)))
if 0<=t<=T:
    print("Высота = %6.2f м" % h)
else:
    print('error')