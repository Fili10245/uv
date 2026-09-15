"""euler.py -- Metodo de Euler para EDO y' = f(x, y). Chapra cap. 25."""


def euler(f, x0, y0, xf, n):
    h = (xf - x0) / n
    xs, ys = [x0], [y0]
    x, y = x0, y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys


if __name__ == "__main__":
    import math
    # y' = y, y(0) = 1  ->  solucion exacta e^x
    xs, ys = euler(lambda x, y: y, 0, 1, 1, 10)
    print(f"y(1) Euler = {ys[-1]:.6f}   (e = {math.e:.6f})")
