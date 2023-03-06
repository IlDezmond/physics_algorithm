from PyQt5 import QtWidgets
from design import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import sys, math
from PyQt5.QtCore import Qt, QSize
import numpy as np
import matplotlib.pyplot as plt


def function(x, t):
    return math.sin(t)/x


def simpson(f, a, b, t):
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
            s = s + f(x, t) + 4 * f(x + h / 2, t) + f(x + h, t)
        s = h/6 * s
        n *= 2
        cond = s1 - s
    return s, n


def main1():
    application.ui.textEdit.clear()
    application.ui.textEdit.append("t                                     S                           N")
    result = []
    for i in range(1, 11):
        result.append(simpson(function, 0.1, 15, i))
    n = 1
    for i in result:
        application.ui.textEdit.append(str(n) + "\t\t" + str(round(i[0], 5)) + "\t\t" + str(i[1]))
        n += 1


def main2():
    result2 = []
    for i in np.arange(0.05, 10, 0.05):
        result2.append(simpson(function, 0.1, 15, i)[0])
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(result2)
    ax.grid(True)
    filename = 'Plot.png'
    plt.savefig(filename, dpi=300)
    pix = QPixmap("Plot.png")
    pix = pix.scaled(QSize(652, 489), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    application.ui.label_4.setPixmap(pix)


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
application.setWindowTitle('Вычисление интеграла')
application.show()
application.ui.pushButton.clicked.connect(main1)
application.ui.pushButton_3.clicked.connect(main2)
application.ui.pushButton_2.clicked.connect(application.close)
sys.exit(app.exec())
