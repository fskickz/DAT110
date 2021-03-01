import math

side1 = float(input('Lengde side 1:'))
side2 = float(input('Lengde side 2:'))
vinkel = float(input('Vinkel mellom sider:'))

areal = 0.5 * (side1) * (side2) * (math.sin(math.radians(vinkel)))
print(areal)
