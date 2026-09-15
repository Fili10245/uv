# Código — Métodos Numéricos (TCIN 18004)

Implementaciones de cada método del curso, en **MATLAB** (`matlab/`) y **Python**
(`python/`). Basadas en Chapra & Canale, *Métodos numéricos para ingenieros* (7.ª ed.)
y Sauer, *Numerical Analysis* (3.ª ed.).

Los archivos de Python **no requieren librerías externas** (solo la biblioteca
estándar), así que corren con solo `python3 archivo.py`. Cada uno trae un ejemplo
ejecutable al final.

## Índice por semana

| Semana | Tema | MATLAB | Python |
|--------|------|--------|--------|
| 1  | Errores de máquina        | `epsilon_maquina.m`     | `epsilon_maquina.py` |
| 2  | Error absoluto/relativo   | `error_relativo.m`      | `error_relativo.py` |
| 3  | Bisección                 | `biseccion.m`           | `biseccion.py` |
| 4  | Falsa posición / punto fijo | `falsa_posicion.m`, `punto_fijo.m` | `falsa_posicion.py`, `punto_fijo.py` |
| 5  | Newton-Raphson / secante  | `newton_raphson.m`, `secante.m` | `newton_raphson.py`, `secante.py` |
| 7  | Gauss                     | `gauss.m`               | `gauss.py` |
| 8  | Gauss-Jordan / no lineales | `gauss_jordan.m`, `newton_sistemas.m` | `gauss_jordan.py`, `newton_sistemas.py` |
| 9  | Regresión lineal          | `minimos_cuadrados.m`   | `minimos_cuadrados.py` |
| 10 | Interpolación de Newton   | `interp_newton.m`       | `interp_newton.py` |
| 11 | Interpolación de Lagrange | `interp_lagrange.m`     | `interp_lagrange.py` |
| 12 | Derivación numérica       | `diferencias_finitas.m` | `diferencias_finitas.py` |
| 13 | Integración (trapecio/Simpson) | `trapecio.m`, `simpson.m` | `trapecio.py`, `simpson.py` |
| 14 | EDO: Euler / Heun         | `euler.m`, `heun.m`     | `euler.py`, `heun.py` |
| 15 | EDO: Runge-Kutta (RK4)    | `runge_kutta.m`         | `runge_kutta.py` |

## Ejemplos rápidos

MATLAB:
```matlab
[r, n] = biseccion(@(x) x.^3 - x - 2, 1, 2, 1e-6, 100);
```

Python:
```bash
python3 python/biseccion.py
```
