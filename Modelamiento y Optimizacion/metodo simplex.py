# Importar la función linprog de scipy.optimize
import scipy.optimize as opt


# Coeficientes de la función objetivo
# La función objetivo es f(x, y) = 4x + 5y. 
# Para convertirla en una minimización, usamos -4 y -5 como coeficientes.
c = [-4, -5]  # Cambio de signo para la maximización

# Coeficientes de las restricciones de desigualdad
# Cada sublista representa los coeficientes de x e y para una restricción.
A = [
    [2, 4],  # Coeficientes para 2x + 4y <= 12
    [5, 3],  # Coeficientes para 5x + 3y <= 15
    [2, 2]   # Coeficientes para 2x + 2y <= 7
]

# Lado derecho de las restricciones de desigualdad
b = [12, 15, 7]

# Límites para cada variable (x, y)
# Dado que x, y >= 0, establecemos el límite inferior en 0 y el superior en None (sin límite superior)
x_bounds = (0, None)
y_bounds = (0, None)

# Resolver el problema de optimización
# method='highs' utiliza el solver HiGHS, adecuado para problemas de optimización lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Imprimir los resultados
print(f"Resultado de la optimización: {result}")
print(f"Valores óptimos de x y y: {result.x}")
print("Este script maximiza la función objetivo 4x + 5y sujeta a las restricciones dadas. " 
      "Se convierte el problema de maximización a minimización cambiando el signo de la función objetivo. "
      "Luego, se definen las restricciones y se resuelve el problema usando el solver 'highs'. "
      "Los valores óptimos de x e y que maximizan la función bajo las restricciones son mostrados al final.")

#2
# Importar la función linprog de scipy.optimize
from scipy.optimize import linprog

# Coeficientes de la función objetivo para el problema 2
c = [-1, -1]  # Cambio de signo para la maximización

# Coeficientes de las restricciones de desigualdad para el problema 2
A = [
    [2, 2],  # Coeficientes para 2x + 2y <= 6
    [2, 1]   # Coeficientes para 2x + y <= 4
]

# Lado derecho de las restricciones de desigualdad para el problema 2
b = [6, 4]

# Límites para cada variable (x, y) son los mismos que antes
x_bounds = (0, None)
y_bounds = (0, None)

# Resolver el problema de optimización
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Imprimir los resultados para el problema 2
print(f"Resultado de la optimización para el problema 2: {result}")
print(f"Valores óptimos de x y y para el problema 2: {result.x}")
print("Este script maximiza la función objetivo x + y sujeta a las restricciones dadas para el problema 2. " 
      "Al igual que antes, se convierte el problema de maximización a minimización cambiando el signo de la función objetivo. "
      "Se definen las restricciones específicas del problema 2 y se resuelve el problema usando el solver 'highs'. "
      "Los valores óptimos de x e y que maximizan la función bajo las restricciones son mostrados al final.")

#3
# Importar la función linprog de scipy.optimize
from scipy.optimize import linprog

# Coeficientes de la función objetivo para el problema 3
c = [-2, -1]  # Cambio de signo para la maximización

# Coeficientes de las restricciones de desigualdad para el problema 3
A = [
    [1, 2],  # Coeficientes para x + 2y <= 6
    [1, -1], # Coeficientes para x - y <= 4
    [1, 0]   # Coeficientes para x <= 2
]

# Lado derecho de las restricciones de desigualdad para el problema 3
b = [6, 4, 2]

# Límites para cada variable (x, y) son los mismos que antes
x_bounds = (0, None)
y_bounds = (0, None)

# Resolver el problema de optimización
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Imprimir los resultados para el problema 3
print(f"Resultado de la optimización para el problema 3: {result}")
print(f"Valores óptimos de x y y para el problema 3: {result.x}")
print("Este script maximiza la función objetivo 2x + y sujeta a las restricciones dadas para el problema 3. "
      "La maximización se convierte en minimización cambiando el signo de la función objetivo. "
      "Se especifican las restricciones del problema y se resuelve utilizando el solver 'highs'. "
      "Los valores óptimos de x e y que maximizan la función bajo las restricciones son mostrados al final.")

4#
import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de x1
x1 = np.linspace(0, 10, 400)

# Restricciones
x2_1 = (12 - 2*x1) / 4  # 2x1 + 4x2 <= 12
x2_2 = x1 - 4           # x2 - x1 >= -4
x2_3 = np.minimum(x2_1, 2)  # x2 <= 2 y combinación con 2x1 + 4x2 <= 12

# Crear el gráfico
plt.figure(figsize=(8, 6))

# Área de restricciones
plt.fill_between(x1, np.maximum(x2_2, 0), x2_3, where=(x2_3>=np.maximum(x2_2, 0)), color='grey', alpha=0.3)

# Líneas de restricciones
plt.plot(x1, x2_1, label=r'$2x_1 + 4x_2 \leq 12$')
plt.plot(x1, x2_2, label=r'$x_2 - x_1 \geq -4$')
plt.axhline(y=2, color='r', linestyle='-', label=r'$x_2 \leq 2$')

# Configuraciones del gráfico
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

# Añadir leyendas
plt.legend()

# Mostrar el gráfico
plt.show()

print("El gráfico muestra las restricciones del problema 4 y la región factible en gris. "
      "Para encontrar la solución óptima de maximización, se debe mover la función objetivo (no mostrada aquí) "
      "a lo largo de la dirección de aumento hasta que toque el último punto de la región factible.")
