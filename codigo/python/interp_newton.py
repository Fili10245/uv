"""interp_newton.py -- Interpolacion por diferencias divididas de Newton. Chapra cap. 18."""


def coef_newton(x, y):
    """Coeficientes (diferencias divididas) del polinomio de Newton."""
    n = len(x)
    c = y[:]                              # copia
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            c[i] = (c[i] - c[i - 1]) / (x[i] - x[i - j])
    return c


def eval_newton(c, x_datos, xq):
    """Evalua el polinomio de Newton en xq (forma anidada de Horner)."""
    n = len(c)
    p = c[n - 1]
    for k in range(n - 2, -1, -1):
        p = p * (xq - x_datos[k]) + c[k]
    return p


if __name__ == "__main__":
    x = [1, 2, 4, 5]
    y = [0, 1, 2, 3]
    c = coef_newton(x, y)
    for xv in [3, 4.5]:
        print(f"P({xv}) = {eval_newton(c, x, xv):.6f}")
