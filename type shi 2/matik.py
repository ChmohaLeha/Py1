import numpy as np

a = 2.493
b = 0.911

#muutto radiaaneiksi
c = 137.7
d = 62.3

#tauliuk
e = [30, 45, 60, 90, 120, 150, 180, 270, 360]

for i in e:
    print(np.radians(i))


print(np.deg2rad(c))
print(np.deg2rad(d))

print(np.degrees(a))
print(np.degrees(b))


k = 1.6
k1 = 2.3
print(np.hypot(k, k1))

