"""epsilon_maquina.py -- Epsilon de maquina y errores de redondeo. Chapra cap. 3."""
import sys


def epsilon_maquina():
    """Menor numero eps tal que 1 + eps > 1 en punto flotante."""
    eps = 1.0
    while (1.0 + eps) > 1.0:
        eps /= 2.0
    return eps * 2.0


if __name__ == "__main__":
    print(f"Epsilon de maquina calculado: {epsilon_maquina():.3e}")
    print(f"sys.float_info.epsilon:       {sys.float_info.epsilon:.3e}")
    print(f"0.1 + 0.2 == 0.3 ? {0.1 + 0.2 == 0.3}")
    print(f"0.1 + 0.2 = {0.1 + 0.2:.17f}")
