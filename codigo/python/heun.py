"""heun.py -- Metodo de Heun (predictor-corrector) para EDO. Chapra cap. 25."""


def heun(f, x0, y0, xf, n):
    h = (xf - x0) / n
    xs, ys = [x0], [y0]
    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        y_pred = y + h * k1               # predictor (Euler)
        k2 = f(x + h, y_pred)
        y += h * (k1 + k2) / 2            # corrector (promedio de pendientes)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys


if __name__ == "__main__":
    import math
    xs, ys = heun(lambda x, y: y, 0, 1, 1, 10)
    print(f"y(1) Heun = {ys[-1]:.6f}   (e = {math.e:.6f})")
