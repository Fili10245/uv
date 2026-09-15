"""newton_sistemas.py -- Newton-Raphson para sistemas no lineales. Sauer cap. 2."""


def _solve(A, b):
    """Resuelve A x = b por eliminacion gaussiana con pivoteo."""
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for k in range(n - 1):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))
        M[k], M[p] = M[p], M[k]
        for i in range(k + 1, n):
            f = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= f * M[k][j]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - s) / M[i][i]
    return x


def jacobiano(F, x, h=1e-8):
    """Jacobiano numerico de F en x por diferencias finitas."""
    n = len(x)
    fx = F(x)
    J = [[0.0] * n for _ in range(n)]
    for j in range(n):
        xj = x[:]
        xj[j] += h
        fxj = F(xj)
        for i in range(n):
            J[i][j] = (fxj[i] - fx[i]) / h
    return J


def newton_sistemas(F, x0, tol=1e-10, maxit=50):
    x = x0[:]
    for it in range(1, maxit + 1):
        Fx = F(x)
        J = jacobiano(F, x)
        dx = _solve(J, [-v for v in Fx])       # resuelve J dx = -F
        x = [x[i] + dx[i] for i in range(len(x))]
        if max(abs(d) for d in dx) < tol:
            return x, it
    return x, maxit


if __name__ == "__main__":
    # Sistema:  x^2 + y^2 = 4 ;  x*y = 1
    F = lambda v: [v[0]**2 + v[1]**2 - 4, v[0] * v[1] - 1]
    sol, n = newton_sistemas(F, [2.0, 0.5])
    print("Solucion:", [round(v, 6) for v in sol], "en", n, "iteraciones")
