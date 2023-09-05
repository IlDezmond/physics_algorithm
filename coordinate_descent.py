"""минимум этой функции находится в точке [0,0,0,0]. ответ получаетсся в пределах погрешности.
использованный метод - метод координатного спуска"""

def f(x):
    return ((x[0]+10*x[1])**2)+((5*(x[2]-x[3]))**2)+((x[1]+2*x[2])**4)+(10*(x[0]-x[3])**4)


x0 = [3, 2, 1, 3]


def cordmin(xx):
    fun = f(xx)
    dx = 0.1
    while dx > 0.0000001:
        cond = 1
        while cond != 0:
            cond = 0
            for i in range(len(xx)):
                xx1 = list(xx)
                xx1[i] += dx
                xx2 = list(xx)
                xx2[i] -= dx
                fun1 = f(xx1)
                fun2 = f(xx2)
                if fun1 < fun:
                    xx = xx1
                    fun = fun1
                    cond += 1
                elif fun2 < fun:
                    xx = xx2
                    fun = fun2
                    cond += 1
                else:
                    pass
        dx = dx / 10
    print(xx)


cordmin(x0)
