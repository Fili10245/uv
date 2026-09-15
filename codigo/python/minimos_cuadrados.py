"""minimos_cuadrados.py -- Regresion lineal por minimos cuadrados. Chapra cap. 17."""


def minimos_cuadrados(x, y):
    """Ajusta y = m x + b. Devuelve (m, b, r2)."""
    n = len(x)
    Sx, Sy = sum(x), sum(y)
    Sxy = sum(xi * yi for xi, yi in zip(x, y))
    Sxx = sum(xi * xi for xi in x)
    m = (n * Sxy - Sx * Sy) / (n * Sxx - Sx**2)
    b = (Sy - m * Sx) / n
    ybar = Sy / n
    ss_res = sum((yi - (m * xi + b))**2 for xi, yi in zip(x, y))
    ss_tot = sum((yi - ybar)**2 for yi in y)
    r2 = 1 - ss_res / ss_tot
    return m, b, r2


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5]
    m, b, r2 = minimos_cuadrados(x, y)
    print(f"y = {m:.4f} x + {b:.4f}   (r^2 = {r2:.4f})")
