"""falsa_posicion.py -- Metodo de la falsa posicion (regula falsi). Chapra cap. 5."""


def falsa_posicion(f, a, b, tol=1e-6, maxit=100):
    if f(a) * f(b) > 0:
        raise ValueError("No hay cambio de signo en [a, b].")
    c = a
    for i in range(1, maxit + 1):
        c_old = c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))   # interseccion con el eje x
        if f(c) == 0:
            return c, i
        if i > 1 and abs((c - c_old) / c) < tol:
            return c, i
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, maxit


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    raiz, n = falsa_posicion(f, 1, 2)
    print(f"Raiz ~= {raiz:.6f} en {n} iteraciones")
