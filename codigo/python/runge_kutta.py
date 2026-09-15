"""runge_kutta.py -- Metodo de Runge-Kutta de 4.o orden (RK4). Chapra cap. 25."""


def rk4(f, x0, y0, xf, n):
    h = (xf - x0) / n
    xs, ys = [x0], [y0]
    x, y = x0, y0
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h,     y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys


if __name__ == "__main__":
    import math
    xs, ys = rk4(lambda x, y: y, 0, 1, 1, 10)
    print(f"y(1) RK4 = {ys[-1]:.8f}   (e = {math.e:.8f})")
