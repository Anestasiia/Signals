import numpy as np

from function import function as f
import constants as const

def deviation(x, y):

    delta = np.zeros(const.n)

    for i in range(const.n):
        delta[i] = abs(f(x[i]) - y[i]) / abs(f(x[i]))

    print_deviation(x, delta)

    return delta

def print_deviation(x, delta):
    print('\nВідносна похибка:\n')
    for i in range(const.n):
        print("x = " + str(x[i]) + " delta = " + str(delta[i]))
    print('-------------------------------------------')