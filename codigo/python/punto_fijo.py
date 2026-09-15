"""punto_fijo.py -- Iteracion de punto fijo x = g(x). Chapra cap. 6."""
import math


def punto_fijo(g, x0, tol=1e-6, maxit=100):
    x = x0
    for i in range(1, maxit + 1):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    return x, maxit


if __name__ == "__main__":
    # Resolver x = cos(x)  ->  g(x) = cos(x)
    raiz, n = punto_fijo(math.cos, 0.5)
    print(f"Raiz de x = cos(x): {raiz:.8f} en {n} iteraciones")
