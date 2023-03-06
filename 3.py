import math


def x1(y):
    return y**(1/3)


def y1(x):
    return math.sqrt(1-x**2)


e = 0.00001

x0 = 0.8
y0 = 0.5


cond = 1

while (cond >= e):
    x_local = x0
    y_local = y0
    x0 = x1(y_local)
    y0 = y1(x_local)
    cond = max(abs(x0 - x_local), abs(y0 - y_local))

print("X = ", round(x0, 4),  "\nY = ", round(y0, 4))
