import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Definición de la función objetivo (área del rectángulo)
def area(x):
    return -(x * (1 - x))  # Negativo porque vamos a minimizar

# Restricción de perímetro
constraints = ({'type': 'eq', 'fun': lambda x: x + (1 - x) - 1})

# Búsqueda de la solución
solution = minimize(area, 0.5, constraints=constraints)
x_opt = solution.x[0]
y_opt = 1 - x_opt
area_opt = -solution.fun

# Resultados
print(f'Dimensiones óptimas: x = {x_opt}, y = {y_opt}')
print(f'Área máxima: {area_opt}')

# Gráfica
x = np.linspace(0, 1, 100)
y = 1 - x
areas = x * y

plt.plot(x, areas, label='Área del rectángulo')
plt.scatter([x_opt], [area_opt], color='red', zorder=5, label='Máximo')
plt.title('Maximización del área del rectángulo')
plt.xlabel('x')
plt.ylabel('Área')
plt.legend()
plt.grid(True)
plt.show()
