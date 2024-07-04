import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coeficientes de la función objetivo (beneficio por unidad)
c = [-10, -15]  # Negativo porque linprog minimiza por defecto

# Coeficientes de las restricciones
A = [
    [4, 7],  # Horas-hombre
    [3, 6]   # Horas-máquina
]

# Lados derechos de las restricciones
b = [300, 500]

# Resolver el problema de optimización
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Resultados óptimos
x1_opt, x2_opt = result.x
beneficio_opt = -result.fun

# Resultados
print(f'Producción óptima: x1 = {x1_opt}, x2 = {x2_opt}')
print(f'Beneficio máximo: {beneficio_opt} euros')

# Gráfica
fig, ax = plt.subplots()
x = np.linspace(0, 100, 400)
y1 = (300 - 4*x) / 7
y2 = (500 - 3*x) / 6

ax.plot(x, y1, label='4x1 + 7x2 ≤ 300 (Horas-hombre)')
ax.plot(x, y2, label='3x1 + 6x2 ≤ 500 (Horas-máquina)')

# Sombrear la región factible
y = np.minimum(y1, y2)
ax.fill_between(x, 0, y, where=(y>0), color='grey', alpha=0.5)

# Solución óptima
ax.plot(x1_opt, x2_opt, 'ro', label='Máximo beneficio')

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xlabel('Producción de x1 (Artículo 1)')
ax.set_ylabel('Producción de x2 (Artículo 2)')
ax.legend()
ax.grid(True)
plt.title('Maximización del beneficio')
plt.show()
