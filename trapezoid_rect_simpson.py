import math


def function(x):
    return math.cos(x)/x


def trapezoid(f, a, b):
    n = 3000
    h = (b - a) / n
    x = a
    s = 0
    for i in range(n-1):
        x += h
        s = s + f(x)
    s = (((f(a) + f(b)) / 2) + s) * h
    return s


def rect(f, a, b):
    n = 3000
    h = (b - a) / n
    x = a + h / 2
    s = 0
    for i in range(n):
        s = s + f(x)
        x = x + h

    s = s * h
    return s


def simpson(f, a, b):
    n = 5000
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + i * h
        s = s + f(x) + 4 * f(x + h / 2) + f(x + h)
    s = h/6 * s
    return s


print("Метод трапеций:                ", trapezoid(function, 0.1, 15))
print("Метод Симпсона:                ", simpson(function, 0.1, 15))
print("Метод средних прямоугольников: ", rect(function, 0.1, 15))

