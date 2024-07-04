import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Definir la función
def f(variables):
    x, y, z = variables
    return x**2 + y**2 - 3*x - 3*x*z + 3*z**2

# Derivadas parciales (gradiente)
def grad_f(variables):
    x, y, z = variables
    df_dx = 2*x - 3 - 3*z
    df_dy = 2*y
    df_dz = -3*x + 6*z
    return np.array([df_dx, df_dy, df_dz])

# Punto inicial para la optimización
x0 = [0, 0, 0]

# Uso de minimize para encontrar los puntos críticos
result = minimize(f, x0, jac=grad_f, method='BFGS')
extremo_relativo = result.x
valor_extremo = result.fun

print("Punto crítico (x, y, z):", extremo_relativo)
print("Valor de la función en el punto crítico:", valor_extremo)

# Crear una malla para graficar la función en x y z manteniendo y constante
x_vals = np.linspace(-10, 10, 400)
z_vals = np.linspace(-10, 10, 400)
X, Z = np.meshgrid(x_vals, z_vals)
Y = 0  # Fijamos y en 0
F = X**2 + Y**2 - 3*X - 3*X*Z + 3*Z**2

# Gráfico de la función
plt.figure(figsize=(10, 8))
cp = plt.contourf(X, Z, F, levels=50, cmap='viridis')
plt.colorbar(cp)
plt.scatter(extremo_relativo[0], extremo_relativo[2], color='red', marker='o')
plt.title('Extremos relativos de la función f(x, z) = x^2 + y^2 - 3x - 3xz + 3z^2 (y = 0)')
plt.xlabel('x')
plt.ylabel('z')
plt.show()
