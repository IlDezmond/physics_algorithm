import numpy as np
from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow
import sys


matrix1 = np.array([[1, 2, 1, 4], [3, -5, 3, 1], [2, 7, -1, 8]])


def gauss(matrix):
    sorted_matrix = np.array(sorted(matrix, key=lambda x: x[0])[::-1], dtype=float)
    if abs(sorted_matrix[0, 0]) < abs(sorted_matrix[-1, 0]):
        np.roll(sorted_matrix, 1, axis=0)
    i = 0
    j = 0
    while i < sorted_matrix.shape[0]:
        i1 = i + 1
        mult = (1 / sorted_matrix[i, j])
        sorted_matrix[i] = sorted_matrix[i] * mult
        while i1 < sorted_matrix.shape[0]:
            sorted_matrix[i1] = sorted_matrix[i1] - (sorted_matrix[i] * sorted_matrix[i1, j])
            i1 += 1
        j += 1
        i += 1
    i = -1
    j = -1
    while abs(i) < sorted_matrix.shape[0]:
        i1 = i - 1
        while abs(i1) <= sorted_matrix.shape[0]:
            sorted_matrix[i1] = sorted_matrix[i1] - (sorted_matrix[i] * sorted_matrix[i1, j - 1])
            i1 -= 1
        j -= 1
        i -= 1
    return sorted_matrix


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    quit()


sys.excepthook = log_uncaught_exceptions


def main():
    if (abs(root_matrix[0, 3] - round(root_matrix[0, 3]))) < 0.0000001:
        root_matrix[0, 3] = round(root_matrix[0, 3])
    if (abs(root_matrix[1, 3] - round(root_matrix[1, 3]))) < 0.0000001:
        root_matrix[1, 3] = round(root_matrix[1, 3])
    if (abs(root_matrix[2, 3] - round(root_matrix[2, 3]))) < 0.0000001:
        root_matrix[2, 3] = round(root_matrix[2, 3])
    application.ui.label_13.setText(str(root_matrix[0, 3]))
    application.ui.label_14.setText(str(root_matrix[1, 3]))
    application.ui.label_15.setText(str(root_matrix[2, 3]))


def set_labels():
    application.ui.label.setText(str(matrix1[0, 0]))
    application.ui.label_2.setText(str(matrix1[0, 1]))
    application.ui.label_3.setText(str(matrix1[0, 2]))
    application.ui.label_4.setText(str(matrix1[1, 0]))
    application.ui.label_5.setText(str(matrix1[1, 1]))
    application.ui.label_6.setText(str(matrix1[1, 2]))
    application.ui.label_7.setText(str(matrix1[2, 0]))
    application.ui.label_8.setText(str(matrix1[2, 1]))
    application.ui.label_9.setText(str(matrix1[2, 2]))
    application.ui.label_10.setText(str(matrix1[0, 3]))
    application.ui.label_11.setText(str(matrix1[1, 3]))
    application.ui.label_12.setText(str(matrix1[2, 3]))


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


root_matrix = gauss(matrix1)

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
set_labels()
application.ui.pushButton.clicked.connect(main)
application.ui.pushButton_2.clicked.connect(application.close)

sys.exit(app.exec())

