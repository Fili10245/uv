"""gauss.py -- Eliminacion gaussiana con pivoteo parcial. Chapra cap. 9."""


def gauss(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]   # matriz aumentada [A|b]
    for k in range(n - 1):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))   # pivoteo parcial
        if p != k:
            M[k], M[p] = M[p], M[k]
        for i in range(k + 1, n):
            factor = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= factor * M[k][j]
    x = [0.0] * n                                      # sustitucion hacia atras
    for i in range(n - 1, -1, -1):
        s = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - s) / M[i][i]
    return x


if __name__ == "__main__":
    A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    b = [7.85, -19.3, 71.4]
    print("Solucion:", [round(v, 6) for v in gauss(A, b)])
