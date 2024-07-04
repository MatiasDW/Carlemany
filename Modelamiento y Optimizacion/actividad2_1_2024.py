import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    x1, x2 = x
    return x1 * x2 * (x1 - 1)

# Derivadas parciales (gradiente)
def grad_f(x):
    x1, x2 = x
    df_dx1 = x2 * (2*x1 - 1)
    df_dx2 = x1 * (x1 - 1)
    return np.array([df_dx1, df_dx2])

# Punto inicial para la optimización
x0 = [0, 0]

# Uso de minimize para encontrar los puntos críticos
result = minimize(f, x0, jac=grad_f, method='BFGS')
extremo_relativo = result.x
valor_extremo = result.fun

print("Punto crítico (x1, x2):", extremo_relativo)
print("Valor de la función en el punto crítico:", valor_extremo)

# Crear una malla para graficar la función
x1_vals = np.linspace(-1, 2, 400)
x2_vals = np.linspace(-1, 2, 400)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = X1 * X2 * (X1 - 1)

# Gráfico de la función
plt.figure(figsize=(8, 6))
cp = plt.contourf(X1, X2, Z, levels=50, cmap='viridis')
plt.colorbar(cp)
plt.scatter(extremo_relativo[0], extremo_relativo[1], color='red', marker='o')
plt.title('Extremos relativos de la función f(x1, x2) = x1 * x2 * (x1 - 1)')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
