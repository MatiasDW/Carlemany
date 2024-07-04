import numpy as np

# Definir los coeficientes c y el término independiente b
c = np.array([1, -2, 3])
b = 4

# Definir la función
def f(x):
    return np.dot(c, x) + b

# Derivadas parciales (gradiente)
def grad_f(x):
    return c

# Verificación de las derivadas parciales
x0 = np.zeros(len(c))  # Punto inicial arbitrario
gradiente = grad_f(x0)

print("Gradiente de la función en el punto inicial:", gradiente)

# Comprobación de la existencia de extremos relativos
if np.all(gradiente == 0):
    print("Existen extremos relativos en los puntos donde el gradiente es cero.")
else:
    print("No existen extremos relativos en un espacio no acotado para una función lineal.")
