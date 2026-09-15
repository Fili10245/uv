"""newton_raphson.py -- Metodo de Newton-Raphson. Chapra cap. 6; Sauer cap. 1."""


def newton_raphson(f, df, x0, tol=1e-8, maxit=50):
    x = x0
    for i in range(1, maxit + 1):
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivada nula; el metodo falla.")
        x_new = x - f(x) / dfx
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    return x, maxit


if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    df = lambda x: 3 * x**2 - 1
    raiz, n = newton_raphson(f, df, 1.5)
    print(f"Raiz ~= {raiz:.8f} en {n} iteraciones")
