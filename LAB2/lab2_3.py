import json
from math import cos, sin, pi
import numpy as np


def load_coefficients(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    coefficients = [(coeff['A'], coeff['B']) for coeff in data['coefficients']]

    return coefficients


def calculate_signal(coefficients):
    signal = np.zeros(len(coefficients), dtype=complex)
    for i in range(len(coefficients)):
        for k, (A, B) in enumerate(coefficients):
            angle = 2 * pi * k * i / len(coefficients)
            signal[i] += (A + 1j * B) * (cos(angle) + 1j * sin(angle))

    return signal


def main():
    filename = "coefficients.json"
    coefficients = load_coefficients(filename)

    for i, (A, B) in enumerate(coefficients):
        print(f"C{i} = {A} + i*{B}")

    signal = calculate_signal(coefficients)
    print(f"Signal: {signal.real.round(decimals=0)}")


if __name__ == "__main__":
    main()