import matplotlib.pyplot as plt
import numpy as np
import math
import decimal
import random

# seq = ["ACGT" for i in range(160)]
# seq = list("".join(seq))
# random.seed(10)
# random.shuffle(seq)      #random sequence
seq = "gttcaaggttacccatctcaagtagcctagcaacatttgcaacatcccaatggccctgtccttttctttactgatggccgtgctggtgctcagctacaaatccatctgttctctaggctgtgatctgcctcagacccacagcctgg\
gtaataggagggccttgatactcctggcacaaatgggaagaatctctcctttctcctgcctgaaggacagacatgactttggacttccccaggaggagtttgatggcaaccagttccagaagactcaagccatctctgtcctccatgagatgat\
ccagcagaccttcaatctcttcagcacagaggactcatctgctgcttgggaacagagcctcctagaaaaattttccactgaactttaccagcaactgaataacctggaagcatgtgtgatacaggaggttgggatggaagagactcccctgatg\
aatgaggactccatcctggctgtgaggaaatacttccaaagaatcactctttatctaacagagaagaaatacagcccttgtgcctgggaggttgtcagagcagaaatcatgagatctctctctttttcaacaaacttgcaaaaaatattaagga\
ggaaggattgaaaactggttcaacatggcaatgatcctgattgactaatacattatctcacactttcatgagttcctccatttcaaagactcacttctataaccaccacgagttgaatcaaaattttcaaatgttttcagcagtgtaaagaagc\
gtcgtgtatacctgtgcaggcactagtactttacagatgaccatgctgatgtctctgttcatctatttatttaaatatttatttaattatttttaagatttaaattatttttttatgtaatatcatgtgtacctttacattgtggtgaatgtaac\
aatatatgttcttcatatttagccaatatattaatttcctttttcattaaatttttactatac".upper()  #real sequence

dx = 900
R = {"A": 5.8, "T": 4.8, "G": 5.7, "C": 4.7}
V = {"A": 2.09, "T": 1.43, "G": 3.12, "C": 2.12}
I = {"A": 7.61, "T": 4.86, "G": 8.22, "C": 4.11}


def in_cond(x):
    return 4 * math.atan(decimal.Decimal(-x + 10 + dx).exp()) - 4 * math.atan(decimal.Decimal(-x + dx).exp())


f_llist = np.array([in_cond(i) for i in range(len(seq))])

df_llist = np.zeros(len(f_llist))

ff_list = np.array(list(zip(f_llist, df_llist)))

XX = np.arange(len(ff_list))


def F(x, base):
    lst = []
    lst.clear()
    for i in range(len(x)):
        if i == 0:
            xx0 = 0
            xx1 = x[i, 0]
            xx2 = x[i + 1, 0]
        elif i == len(x) - 1:
            xx0 = x[i - 1, 0]
            xx1 = x[i, 0]
            xx2 = 0
        else:
            xx0 = x[i - 1, 0]
            xx1 = x[i, 0]
            xx2 = x[i + 1, 0]
        f = (((xx2 - xx1) / 0.65) * R[base] - 0.5 * np.sin(xx1)) * V[base] * 10 ** -1
        lst.append(f)
    x1 = list(x[:, 1])
    return np.array(list(zip(x1, lst)))


def RK4(x, base):
    h = XX[1] - XX[0]
    k1 = h * F(x, base)
    k2 = h * F(x + k1 / 2, base)
    k3 = h * F(x + k2 / 2, base)
    k4 = h * F(x + k3, base)
    X2 = x + ((k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return X2


res = RK4(ff_list, seq[1])

ress = list(res[:, 0])
plt.ion()
fig, ax = plt.subplots()
fig.set_figwidth(10)
line, = ax.plot(XX, ress)
for i in seq:
    res[:, 1] = 0
    res = RK4(res, i)
    ress = list(res[:, 0])
    ress.reverse()
    line.set_ydata(ress)
    fig.canvas.draw()
    fig.canvas.flush_events()

plt.ioff()
plt.show()
