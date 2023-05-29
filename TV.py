import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


def draw_F_and_f(X, S):
    F = lambda x: scipy.stats.norm.cdf((x - X) / S)
    f = lambda x: scipy.stats.norm.pdf((x - X) / S)

    start = X - 3 * S
    end = X + 3 * S
    xx = np.linspace(start, end, 50)
    FF = [F(x) for x in xx]
    ff = [f(x) for x in xx]

    fig1, ax1 = plt.subplots(1, 1)
    plt.xlabel("x")
    plt.ylabel("y")
    ax1.plot(xx, FF, label="Функция распределения")
    ax1.plot(xx, ff, label="Плотность")
    ax1.plot([X, X], [0, 1], color="black", linestyle="--", linewidth=0.8)
    ax1.legend(loc="best", frameon=False)


def draw_n_emp_and_n_th():
    xx = [x for x in range(86, 100, 2)]
    n_emp = [1, 6, 16, 29, 21, 10, 10]
    n_th = [1.767, 6.231, 15.717, 24.552, 22.692, 15.345, 6.696]
    n_th_round = [2, 6, 16, 25, 23, 15, 6]

    fig2, ax2 = plt.subplots(1, 1)
    plt.xlabel("x")
    plt.ylabel("n")
    ax2.plot(xx, n_emp, label="Эмпирические частоты")
    ax2.plot(xx, n_th, label="Теоретические частоты")
    ax2.plot(xx, n_th_round, label="Теоретические частоты (округлённые)")
    for x in xx:
        y_st = 0 if x < 90 else 5 if x < 96 else 2
        ax2.plot(
                [x, x], [y_st, 30], color="black", linestyle="--",
                linewidth=0.8)
    ax2.legend(loc="best", frameon=False)


def draw():
    draw_F_and_f(92.86, 2.83)
    draw_n_emp_and_n_th()
    plt.show()


if __name__ == "__main__":
    draw()
