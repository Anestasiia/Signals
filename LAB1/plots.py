from matplotlib import pyplot as plt
import constants as const

def plots(x, y, ap):
    # Побудова графіку функції
    plt.plot(x, y)
    plt.plot(x, ap)

    # Встановлюємо межі графіку
    plt.xlim([const.a, const.b])
    plt.ylim([-20, 20])

    # Додаємо підписи для осей та заголовок графіку
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Графік функції f(x) = 17 * sin(π*x*17) на інтервалі [0, π]')

    plt.show()