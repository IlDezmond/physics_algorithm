import math
import numpy as np
import matplotlib.pyplot as plt

"""
вот тут Закирьянов меня попросил изменить начальную функцию, ну тоесть Х и У.
тк изначальная функция в задании была слишком прямой и было плохо видно как сплайн накладывается на график.
значения Х и У можешь поменять если хочешь. раскоментируй их и закоментируй другие для этого
и в этом случае так же придётся поменять и саму функцию в коде. она там тоже закоментирована для этого. (func)
так же раскоментируй её и закоментируй другую.
"""

#x = [1.0, 1.5, 2.0, 2.5, 3]                              # изменённые значения
#y = [0.841470, 0.997494, 0.909297, 0.598472, 0.141120]

x = [1.0, 1.1, 1.2, 1.3, 1.4]                          # оригинальные значения из задания
y = [0.000000, 0.095310, 0.182322, 0.262364, 0.336472]


def func(x):
    #return math.sin(x)    # изменённая функция
    return math.log(x)   # оригинальная функия из задания


def df(x, f):
    return (f(x+0.001)-f(x-0.001))/0.002


def spline(x, f, ddf, array_x):
    for i in range(len(array_x)):
        if array_x[i] <= x < array_x[i + 1]:
            xi = array_x[i]
            xi1 = array_x[i + 1]
            h = xi1 - xi
    m = ddf(xi, f)
    m1 = ddf(xi1, f)
    s3 = ((((xi1-x)**2)*(2*(x-xi)+h)/h**3)*f(xi)) + ((((x-xi)**2)*(2*(xi1-x)+h)/h**3)*f(xi1)) \
         + (((((xi1-x)**2)*(x-xi))/h**2)*m) + (((((x-xi)**2)*(x-xi1))/h**2)*m1)
    return s3


for i in range(len(x)-1):
    xx = x[i]+0.05
    print(spline(xx, func, df, x))


end_x1 = x[-1]
y1 = []
x1 = np.arange(1.0, end_x1, 0.01)


# for i in x1:
#     if i != x1[-1]:
#         y1.append(spline(i, func, df, x1))
#
# x1 = np.delete(x1, -1)
#
# plt.plot(x, y, color='#00c0ff')
# plt.scatter(x, y, c='#c543ff')
# plt.plot(x1, y1, color='#ff3830')
# plt.show()
