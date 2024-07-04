#problema 1
from scipy.optimize import linprog

# Coeficientes de la función objetivo (multiplicamos por -1 para maximizar)
c = [-5, -4]

# Coeficientes de las restricciones lineales Ax <= b
A = [[1, 1], [10, 6]]
b = [5, 45]

# Límites de las variables
x_bounds = (0, None)

# Resolución del problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds], method='highs')

# Mostrar los resultados
print(f'Valor óptimo: {-result.fun}, en x1 = {result.x[0]}, x2 = {result.x[1]}')

print("\nPara aplicar el método de Branch and Bound y garantizar soluciones enteras,")
print("se debería realizar una búsqueda iterativa, verificando soluciones enteras cercanas a esta solución óptima lineal,")
print("y explorando ramas de soluciones potenciales hasta encontrar la óptima entera.")

# problema 2
from scipy.optimize import linprog

# Coeficientes de la función objetivo (multiplicamos por -1 para maximizar)
c = [-1, -2]  # Nota: cambiamos los signos para adaptarlos a la minimización

# Coeficientes de las restricciones lineales Ax <= b
A = [[1, -1], [12, 2]]  # Asumiendo "x1 - x2 ≤ 0" y "12x1 + 2x2 ≤ 7"
b = [0, 7]

# Límites de las variables
x_bounds = (0, None)

# Resolución del problema de programación lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, x_bounds], method='highs')

# Mostrar los resultados
print(f'Valor óptimo: {-result.fun}, en x1 = {result.x[0]}, x2 = {result.x[1]}')

print("\nEste script resuelve la versión lineal del segundo problema de optimización propuesto.")
print("La solución óptima lineal puede no cumplir con la restricción de enteros,")
print("por lo que, para garantizar soluciones enteras, sería necesario aplicar manualmente el método de Branch and Bound,")
print("o utilizar una biblioteca específica que soporte optimización entera.")
