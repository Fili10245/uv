"""interp_lagrange.py -- Interpolacion con polinomios de Lagrange. Chapra cap. 18."""


def lagrange(x, y, xq):
    n = len(x)
    total = 0.0
    for i in range(n):
        Li = 1.0
        for j in range(n):
            if j != i:
                Li *= (xq - x[j]) / (x[i] - x[j])
        total += y[i] * Li
    return total


if __name__ == "__main__":
    x = [1, 2, 4, 5]
    y = [0, 1, 2, 3]
    for xv in [3, 4.5]:
        print(f"P({xv}) = {lagrange(x, y, xv):.6f}")
