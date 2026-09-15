"""diferencias_finitas.py -- Derivacion numerica por diferencias finitas. Chapra cap. 23."""
import math


def adelante(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def atras(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h


def centrada(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def segunda(f, x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2


if __name__ == "__main__":
    f, x = math.sin, 1.0
    print(f"f'(1)  centrada = {centrada(f, x):.8f}   (cos 1 = {math.cos(1):.8f})")
    print(f"f''(1)          = {segunda(f, x):.8f}   (-sin 1 = {-math.sin(1):.8f})")
