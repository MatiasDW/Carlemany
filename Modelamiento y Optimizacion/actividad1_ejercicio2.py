import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coeficientes de la función objetivo (coste)
c = [5, 8]

# Coeficientes de las restricciones
A = [
    [2, 3],  # Vitamina A
    [2, 2],  # Vitamina C
    [8, 2]   # Vitamina D
]

# Lados derechos de las restricciones
b = [36, 28, 32]

# Resolver el problema de optimización
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Resultados óptimos
x1_opt, x2_opt = result.x
coste_opt = result.fun

# Resultados
print(f'Combinación óptima: x1 = {x1_opt}, x2 = {x2_opt}')
print(f'Coste mínimo: {coste_opt} euros')

# Gráfica
fig, ax = plt.subplots()
x = np.linspace(0, 20, 200)
y1 = (36 - 2*x) / 3
y2 = (28 - 2*x) / 2
y3 = (32 - 8*x) / 2

ax.plot(x, y1, label='2x1 + 3x2 ≥ 36 (Vitamina A)')
ax.plot(x, y2, label='2x1 + 2x2 ≥ 28 (Vitamina C)')
ax.plot(x, y3, label='8x1 + 2x2 ≥ 32 (Vitamina D)')

# Sombrear la región factible
y = np.minimum(np.minimum(y1, y2), y3)
ax.fill_between(x, y, 20, where=(y>0), color='grey', alpha=0.5)

# Solución óptima
ax.plot(x1_opt, x2_opt, 'ro', label='Solución óptima')

ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_xlabel('x1 (Marca 1)')
ax.set_ylabel('x2 (Marca 2)')
ax.legend()
ax.grid(True)
plt.title('Optimización de Complejos Vitamínicos')
plt.show()
