import math

def f(x):
    return math.cosh(x)+math.cos(x)-3


def secant(x0, x1, e, N):
    step = 1
    condition = True
    while condition:

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Итерации кончились')
            break

        condition = abs(f(x2)) > e
    print('Корень уравнения: %s' % round(x2, 3))


e = 0.001


secant(1.0, 2.0, e, 200)
