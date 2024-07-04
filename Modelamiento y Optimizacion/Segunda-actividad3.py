import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x[0] - 2)**4 + (x[0] - 2*x[1])**2

def grad_f(x):
    dfdx = 4*(x[0] - 2)**3 + 2*(x[0] - 2*x[1])
    dfdy = -4*(x[0] - 2*x[1])
    return np.array([dfdx, dfdy])

def gradient_descent(initial_point, learning_rate, epsilon):
    x = initial_point
    grad = grad_f(x)
    iterations = 0
    while np.linalg.norm(grad) > epsilon:
        x = x - learning_rate * grad
        grad = grad_f(x)
        iterations += 1
    return x, iterations

initial_point = np.array([0, 3])
learning_rate = 0.01
epsilon = 1

optimal_point, iterations = gradient_descent(initial_point, learning_rate, epsilon)
print(f"Optimal point: {optimal_point} found in {iterations} iterations")

# Explicación del procedimiento
print("""
Se utilizó el método del gradiente para minimizar la función dada, partiendo del punto (0, 3) y con un criterio de parada basado en un error menor a 1. 
El gradiente de la función fue calculado y utilizado para iterativamente actualizar el punto hacia el mínimo local. 
El aprendizaje se detuvo cuando la norma del gradiente fue menor que el error especificado.""")

# 2
def f2(x):
    return 2*x[0]**2 + x[1]**2 + 8*x[0] - 6*x[1] + 20

def grad_f2(x):
    dfdx = 4*x[0] + 8
    dfdy = 2*x[1] - 6
    return np.array([dfdx, dfdy])

def gradient_descent_step(x, learning_rate):
    return x - learning_rate * grad_f2(x)

# Parámetros iniciales
initial_point = np.array([-1, 1])
learning_rate = 0.1

# Realizar 3 iteraciones
for i in range(1, 4):
    initial_point = gradient_descent_step(initial_point, learning_rate)
    print(f"Iteración {i}, punto: {initial_point}")

# Explicación del procedimiento
print("""
Para minimizar la función dada, se utilizaron las tres primeras iteraciones del método del gradiente, comenzando desde el punto (-1, 1).
Este método ajusta iterativamente la posición basándose en el gradiente de la función en el punto actual y un tamaño de paso predefinido.""")

#3
def f3(x):
    return x[0] * x[1]

def grad_f3(x):
    return np.array([x[1], x[0]])

def hessian_f3(x):
    return np.array([[0, 1], [1, 0]])

def newton_step(x):
    H_inv = np.linalg.inv(hessian_f3(x))
    return x - np.dot(H_inv, grad_f3(x))

# Parámetros iniciales
initial_point = np.array([0, 1])
epsilon = 0.5
iteration = 0

# Método de Newton con criterio de parada basado en el error
while np.linalg.norm(grad_f3(initial_point)) > epsilon and iteration < 10:
    initial_point = newton_step(initial_point)
    iteration += 1

print(f"Optimal point: {initial_point} found in {iteration} iterations")

# Explicación
print("""
El método de Newton se utilizó para minimizar la función dada, partiendo del punto (0, 1). 
Este método utiliza tanto el gradiente como la matriz Hessiana para encontrar una dirección y magnitud de paso que aproxime mejor al mínimo local.
La iteración se detiene cuando el gradiente es menor que el umbral de error o se alcanza un número máximo de iteraciones.""")

#4
def f4(x):
    return 2*x[0]**2 + x[1]**2 + 8*x[0] - 6*x[1] + 20

def grad_f4(x):
    dfdx1 = 4*x[0] + 8
    dfdx2 = 2*x[1] - 6
    return np.array([dfdx1, dfdx2])

def hessian_f4(x):
    return np.array([[4, 0], [0, 2]])

def newton_step_4(x):
    H_inv = np.linalg.inv(hessian_f4(x))
    return x - np.dot(H_inv, grad_f4(x))

# Parámetros iniciales
initial_point = np.array([-1, 1])

# Realizar 3 iteraciones del método de Newton
for i in range(1, 4):
    initial_point = newton_step_4(initial_point)
    print(f"Iteración {i}, punto: {initial_point}")

# Explicación del procedimiento
print("""
se aplicó el método de Newton para minimizar la función especificada, comenzando desde el punto (-1, 1).
El método de Newton aprovecha el gradiente y la matriz Hessiana de la función para realizar saltos más precisos hacia el mínimo local.
Se realizaron tres iteraciones para aproximar el punto óptimo más cercano al punto de inicio.""")


#5
# ALGORITMO MétodoDelGradiente
# Entrada: Función objetivo f, su gradiente grad_f, punto inicial x0, tasa de aprendizaje alpha, tolerancia epsilon
# Salida: Punto óptimo x_opt

# 1. Inicializar x = x0
# 2. Calcular el gradiente de f en x, grad = grad_f(x)
# 3. Mientras la norma de grad sea mayor que epsilon:
#     3.1. Actualizar x = x - alpha * grad
#     3.2. Recalcular grad = grad_f(x)
# 4. Retornar x como el punto óptimo x_opt

# FIN ALGORITMO

#6
# ALGORITMO MétodoDeNewton
# Entrada: Función objetivo f, su gradiente grad_f, su matriz Hessiana hess_f, punto inicial x0, tolerancia epsilon
# Salida: Punto óptimo x_opt

# 1. Inicializar x = x0
# 2. Calcular el gradiente de f en x, grad = grad_f(x)
# 3. Calcular la inversa de la matriz Hessiana de f en x, H_inv = inv(hess_f(x))
# 4. Mientras la norma de grad sea mayor que epsilon:
#     4.1. Actualizar x = x - H_inv * grad
#     4.2. Recalcular grad = grad_f(x)
#     4.3. Recalcular H_inv = inv(hess_f(x))
# 5. Retornar x como el punto óptimo x_opt

# FIN ALGORITMO

