import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Precios de los productos
p1 = 10
p2 = 15

# Definición de la función de beneficio
def beneficio(x):
    x1, x2 = x
    return -(p1 * x1 + p2 * x2 - (2 * x1**2 + x1 * x2 + 2 * x2**2))

# Inicialización de la búsqueda de la solución
x0 = [0, 0]  # Valores iniciales

# Resolver el problema de optimización
solution = minimize(beneficio, x0, method='BFGS')
x1_opt, x2_opt = solution.x
beneficio_opt = -solution.fun

# Resultados
print(f'Producción óptima: x1 = {x1_opt}, x2 = {x2_opt}')
print(f'Beneficio máximo: {beneficio_opt} euros')

# Gráfica del beneficio en función de x1 y x2
x1_vals = np.linspace(0, 10, 400)
x2_vals = np.linspace(0, 10, 400)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = p1 * X1 + p2 * X2 - (2 * X1**2 + X1 * X2 + 2 * X2**2)

plt.contour(X1, X2, Z, levels=50, cmap='viridis')
plt.colorbar(label='Beneficio')
plt.scatter([x1_opt], [x2_opt], color='red', label='Máximo beneficio')
plt.xlabel('Producción de x1')
plt.ylabel('Producción de x2')
plt.legend()
plt.title('Maximización del beneficio')
plt.grid(True)
plt.show()
