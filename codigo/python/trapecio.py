"""trapecio.py -- Integracion por la regla del trapecio compuesta. Chapra cap. 21."""


def trapecio(f, a, b, n=100):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h


if __name__ == "__main__":
    import math
    I = trapecio(math.sin, 0, math.pi, 1000)
    print(f"Integral de sin en [0, pi] = {I:.8f}   (exacto = 2)")
