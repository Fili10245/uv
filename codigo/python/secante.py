"""secante.py -- Metodo de la secante (Newton sin derivada). Chapra cap. 6."""


def secante(f, x0, x1, tol=1e-8, maxit=50):
    for i in range(1, maxit + 1):
        f0, f1 = f(x0), f(x1)
        x2 = x1 - f1 * (x0 - x1) / (f0 - f1)
        if abs(x2 - x1) < tol:
            return x2, i
        x0, x1 = x1, x2
    return x1, maxit


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    raiz, n = secante(f, 1, 2)
    print(f"Raiz ~= {raiz:.8f} en {n} iteraciones")
