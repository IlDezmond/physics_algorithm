from PyQt5 import QtWidgets
from design import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import sys, math
from PyQt5.QtCore import Qt, QSize


def function(x):
    return math.cos(x)/x


def trapezoid(f, a, b):
    e = float(application.ui.lineEdit.text())
    n = 2
    s = 0
    cond = 10
    while abs(cond) > e:
        h = (b - a) / n
        x = a
        s1 = s
        s = 0
        for i in range(n-1):
            x += h
            s = s + f(x)
        s = (((f(a) + f(b)) / 2) + s) * h
        n *= 2
        cond = s1 - s
    return s, n

def simpson(f, a, b):
    e = float(application.ui.lineEdit.text())
    n = 2
    s = 0
    cond = 10
    while abs(cond) > e:
        s1 = s
        s = 0
        h = (b - a) / n
        for i in range(n):
            x = a + (i) * h
            s = s + f(x) + 4 * f(x + h / 2) + f(x + h)
        s = h/6 * s
        n *= 2
        cond = s1 - s
    return s, n


def main():
    result = trapezoid(function, 0.1, 15)
    result2 = simpson(function, 0.1, 15)
    application.ui.label_5.setText(str(result[0]) + ", " + str(result2[0]))
    application.ui.label_6.setText(str(result[1])+ ", " + str(result2[1]))


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    quit()


sys.excepthook = log_uncaught_exceptions


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = mywindow()

pix = QPixmap("image.png")
pix = pix.scaled(QSize(301, 151), Qt.KeepAspectRatio, Qt.SmoothTransformation)
application.ui.label_7.setPixmap(pix)
application.setWindowTitle('Вычисление интеграла')

application.show()
application.ui.pushButton.clicked.connect(main)
application.ui.pushButton_2.clicked.connect(application.close)
sys.exit(app.exec())
