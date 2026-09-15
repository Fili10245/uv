"""biseccion.py -- Raiz de f en [a, b] por biseccion. Chapra cap. 5; Sauer cap. 1."""


def biseccion(f, a, b, tol=1e-6, maxit=100):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en [a, b].")
    for i in range(1, maxit + 1):
        c = (a + b) / 2.0              # punto medio
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, i
        if f(a) * f(c) < 0:
            b = c                     # la raiz esta en [a, c]
        else:
            a = c                     # la raiz esta en [c, b]
    return (a + b) / 2.0, maxit


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    raiz, n = biseccion(f, 1, 2)
    print(f"Raiz ~= {raiz:.6f} en {n} iteraciones")
