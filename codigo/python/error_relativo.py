"""error_relativo.py -- Errores absoluto, relativo y aproximado. Chapra cap. 3."""
import math


def errores(x_real, x_aprox):
    """Devuelve (error absoluto, error relativo)."""
    ea = abs(x_aprox - x_real)
    er = ea / abs(x_real)
    return ea, er


if __name__ == "__main__":
    ea, er = errores(math.pi, 22 / 7)
    print("Aproximacion 22/7 de pi:")
    print(f"  Error absoluto = {ea:.6e}")
    print(f"  Error relativo = {er:.6e} ({er * 100:.4f}%)")

    # Criterio de paro por error relativo aproximado entre iteraciones
    tol, x_prev, x_curr, k = 1e-4, 1.0, 1.5, 0
    while True:
        k += 1
        erp = abs((x_curr - x_prev) / x_curr)   # error relativo aproximado
        if erp < tol:
            break
        x_prev, x_curr = x_curr, 0.5 * (x_curr + 2 / x_curr)
    print(f"\nRaiz de 2 ~= {x_curr:.8f} en {k} iteraciones (erp < {tol:.0e})")
