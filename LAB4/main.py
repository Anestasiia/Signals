import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

n = 17
d = 21
N = 100 * n


# підпункт b) пункту 1
def f(t):
    return t ** ((2 * n + 1) / 3)


# пункт 1
def compute_fourier_coefficient(k, f, T, N):
    wk = 2 * np.pi * k / T
    re_f = lambda t: np.real(f(t) * np.cos(wk * t))
    im_f = lambda t: np.imag(f(t) * np.sin(wk * t))
    coef_re, _ = quad(lambda t: re_f(t), -N, N)
    coef_im, _ = quad(lambda t: im_f(t), -N, N)
    return coef_re + 1j * coef_im


def compute_ift(f, T, N):
    coefficients = np.zeros(d, dtype=np.complex128)
    for k in range(d):
        C_k = compute_fourier_coefficient(k, f, T, N)
        coefficients[k] = C_k
    return coefficients


# пункт 2
def amplitude_spectrum(coefficients):
    return [np.sqrt(np.real(c) ** 2 + np.imag(c) ** 2) for c in coefficients]


# пункт 3
def plot_result(coefficients, T):
    amplitudes = amplitude_spectrum(coefficients)
    real_parts = [np.real(c) for c in coefficients]

    plt.plot(real_parts)
    plt.title(f"Re F(wk) при T={T}")
    plt.xlabel("k")
    plt.ylabel("Значення")
    plt.grid(True)
    plt.show()

    plt.plot(amplitudes)
    plt.title(f"|F(wk)| при T={T}")
    plt.xlabel("k")
    plt.ylabel("Амплітуда")
    plt.grid(True)
    plt.show()


# побудова графіків при T = 4, 8, 16, 32, 64, 128
t = np.linspace(0.1, 10, 21)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(t, f(t), label=f"n = {n}")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("Plot of f(t) = t ** ((2 * n + 1) / 3)")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
k_values = np.arange(0, 21, 1)

for i in range(2, 8):
    T = 2 ** i
    coef = compute_ift(f, T, N)
    real_parts = [np.real(c) for c in coef]
    plt.plot(k_values, real_parts, marker='o',
             linestyle='-', label=f"T = {T}")

plt.xlabel("k")
plt.ylabel("Re(F(w_k))")
plt.title("Real part of F(w_k) for different T values")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
k_values = np.arange(0, 21, 1)

for i in range(2, 8):
    T = 2 ** i
    coef = compute_ift(f, T, N)
    amplitudes = amplitude_spectrum(coef)
    plt.plot(k_values, amplitudes, marker='o',
             linestyle='-', label=f"T = {T}")

plt.xlabel("k")
plt.ylabel("|F(w_k)|")
plt.title("Amplitude |F(w_k)| for different T values")
plt.grid(True)
plt.legend()
plt.show()
