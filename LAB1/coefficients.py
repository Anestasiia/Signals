import numpy as np
import scipy.integrate as integrate
from function import function
import constants as const


def coefficients():
    b_k = np.zeros(const.n)

    for i in range(1, const.n + 1):
        b_k[i - 1] = 2 / np.pi * \
                     integrate.quad(lambda x: function(x) * np.sin(i * np.pi * x), 0, const.b)[0]

    print_coefficients(b_k)

    return b_k


def print_coefficients(b_k):
    print('\nКоефіцієнти Фур\'є\n')

    for i in range(0, const.n):
        print("b{} = {:.10f}".format(i, b_k[i]))
    print('-------------------------------------------')
