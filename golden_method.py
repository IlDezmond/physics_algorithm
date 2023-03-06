import math


def f(x):
    return x**3 - x + math.exp(-x)


e = 0.01
a = 0
b = 1
golden_f = (1 + math.sqrt(5)) / 2

while True:
    x1 = b - ((b - a) / golden_f)
    x2 = a + ((b - a) / golden_f)
    y1 = f(x1)
    y2 = f(x2)
    if y1 > y2:
        a = x1
    else:
        b = x2
    if abs(b - a) < e:
        x_root = (a + b) / 2
        break

print("Минимум в точке х = ", round(x_root, 5))
