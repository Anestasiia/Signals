import numpy as np
import constants as const
import scipy.integrate as integrate
from function import function


def approximation(b_k, N):
    y = 0

    x = np.arange(-np.pi, np.pi, 2 * np.pi / const.n)

    for i in range(0, const.n):
        y += b_k[i] * np.sin(x * np.pi * (i + 1))

    print_approximation(x, y, N)

    return x, y.round(N)


def print_approximation(x, y, N):
    print('\nЗначення рядом Фур\'є\n')
    for i in range(const.n):
        print("x = " + str(x[i]) + " y = " + str(y[i].round(N)))
    print('-------------------------------------------')
