import math

func = lambda x: 0.1 * x ** 2 - x * math.log(x)

a1, b1 = 1.0, 2.0

e = 0.001


def half_div(a, b, f):
    x = (a + b) / 2
    while abs((b - a)/2) >= e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return (a + b) / 2


print('Корень уравнения %s' % round(half_div(a1, b1, func), 3))
