"""
Multiplicidad de estados estacionarios en un CSTR adiabático (Fogler, cap. 12).
Reacción A -> B de primer orden, irreversible, en fase líquida.

Los estados estacionarios son las intersecciones de:
    G(T) = (-dH) * X_MB(T)     calor generado
    R(T) = Cp * (T - T0)       calor removido (adiabático)
"""
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

# ---- Datos ----
T0  = 320.0     # K, temperatura de alimentación
tau = 10.0      # min, tiempo espacial
k1  = 0.002     # 1/min, constante de velocidad a T1
T1  = 350.0     # K
EoR = 10000.0   # K, energía de activación / R
dH  = -8000.0   # cal/mol, calor de reacción
Cp  = 40.0      # cal/(mol K), suma de Theta_i * Cp_i


def k(T):
    return k1 * np.exp(EoR * (1.0 / T1 - 1.0 / T))


def X_mb(T):
    """Conversión del balance de moles (CSTR, primer orden)."""
    return tau * k(T) / (1.0 + tau * k(T))


def G(T):
    return -dH * X_mb(T)


def R(T):
    return Cp * (T - T0)


def f(T):
    return G(T) - R(T)


# ---- Buscar intersecciones G(T) = R(T) ----
T = np.linspace(T0, 560.0, 2000)
y = f(T)
print("Estados estacionarios:")
for i in range(len(T) - 1):
    if y[i] * y[i + 1] < 0:
        Ts = brentq(f, T[i], T[i + 1])
        # Si G - R pasa de + a -, la pendiente de R supera a la de G: estable
        tipo = "estable" if y[i] > 0 else "inestable"
        print(f"  T = {Ts:6.1f} K   X = {X_mb(Ts):.3f}   ({tipo})")

# ---- Gráfica ----
plt.plot(T, G(T), "r", label="G(T) generado")
plt.plot(T, R(T), "b", label="R(T) removido")
plt.xlabel("T [K]")
plt.ylabel("cal/mol")
plt.title("Multiplicidad de estados estacionarios en un CSTR")
plt.legend()
plt.grid(True)
plt.show()
