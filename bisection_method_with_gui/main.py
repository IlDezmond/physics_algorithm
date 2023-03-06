from PyQt5 import QtWidgets
from design import Ui_MainWindow
import sys
import math

func = lambda x: math.sin(x) * x - 1

e = 0


def scan(a, b, func_in):
    locals_roots = []
    f = func_in
    eps = 0.001
    step = a
    while step <= b:
        if f(step) * f(step + eps) < 0:
            locals_roots.append([step, step + eps])
            step += eps
        else:
            step += eps
    return locals_roots


def half_div(a, b, f):
    x = (a + b) / 2
    while abs((b - a)/2) >= e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    root = (a + b) / 2
    return root, f(root)


def main():
    application.ui.textEdit.clear()
    global e
    e = float(application.ui.lineEdit_3.text())
    start_int = int(application.ui.lineEdit.text())
    end_int = int((application.ui.lineEdit_2.text()))
    scan(start_int, end_int, func)
    roots = []
    n = 1
    for i in scan(start_int, end_int, func):
        try:
            roots.append(half_div(i[0], i[1], func))
        except:
            pass
    for i in roots:
        application.ui.textEdit.append(str(n) + ')\t\t' + str(round(i[0], 5)) + '\t\t' + str(round(i[1], 5)))
        n += 1


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    quit()



sys.excepthook = log_uncaught_exceptions


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
application.ui.pushButton.clicked.connect(main)
application.ui.pushButton_2.clicked.connect(application.close)

sys.exit(app.exec())
