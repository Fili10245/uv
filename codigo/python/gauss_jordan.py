"""gauss_jordan.py -- Gauss-Jordan con pivoteo: solucion e inversa. Chapra cap. 9-10."""


def gauss_jordan(A, b):
    n = len(b)
    # matriz aumentada [A | I | b]
    M = [A[i][:] + [1.0 if i == j else 0.0 for j in range(n)] + [b[i]]
         for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(M[i][k]))   # pivoteo parcial
        if p != k:
            M[k], M[p] = M[p], M[k]
        piv = M[k][k]
        M[k] = [v / piv for v in M[k]]                     # normaliza el pivote
        for i in range(n):
            if i != k:
                factor = M[i][k]
                M[i] = [M[i][j] - factor * M[k][j] for j in range(len(M[i]))]
    inv = [row[n:2 * n] for row in M]
    x = [row[-1] for row in M]
    return x, inv


if __name__ == "__main__":
    A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    b = [7.85, -19.3, 71.4]
    x, inv = gauss_jordan(A, b)
    print("Solucion:", [round(v, 6) for v in x])
