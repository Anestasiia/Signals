import matplotlib.pyplot as plt
import constants as const
import numpy as np

def harmonic(b_k):
    x = np.linspace(0, np.pi, 1000)

    plt.figure(figsize=(14, 10))

    for i in range(1, const.n + 1):
        harmonic = [b_k[i-1] * np.sin(i * val) for val in x]
        plt.plot(x, harmonic, label=f"Грамоніка {i}")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

def spectrum(b_k):
    ks = list(range(30))

    plt.figure(figsize=(10, 6))
    plt.stem(ks[:], b_k[:], "r",
             markerfmt="ro", basefmt=" ", label="|b_n|")
    plt.title("Частотний спектр коефіцієнтів Фур'є")
    plt.xlabel("n")
    plt.ylabel("Амплітуда")
    plt.grid(True)
    plt.legend()
    plt.show()