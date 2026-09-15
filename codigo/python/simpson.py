"""simpson.py -- Integracion por la regla de Simpson 1/3 compuesta. Chapra cap. 21."""


def simpson(f, a, b, n=100):
    if n % 2 == 1:                 # Simpson 1/3 requiere n par
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


if __name__ == "__main__":
    import math
    I = simpson(math.sin, 0, math.pi, 100)
    print(f"Integral de sin en [0, pi] = {I:.10f}   (exacto = 2)")
