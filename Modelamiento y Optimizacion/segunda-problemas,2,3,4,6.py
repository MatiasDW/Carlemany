#2
from scipy.optimize import minimize
import numpy as np

def f2(vars):
    x, y, z = vars
    return x**2 + y**2 + z**2

initial_guess = [1, 1, 1]
result = minimize(f2, initial_guess)

print(f"El punto mínimo se encuentra en: {result.x} con un valor de: {result.fun}")

# Explicación
print("""
Se calculó el extremo relativo (mínimo global) de la función f(x, y, z) = x^2 + y^2 + z^2 utilizando Scipy y Numpy. 
Partiendo de un punto inicial arbitrario, se utilizó el método de optimización 'minimize' para encontrar el punto en el cual la función alcanza su valor mínimo. 
Dado que la función es cuadrática y simétrica en todas sus variables, el mínimo global se encuentra en el origen.""")

#3
from scipy.optimize import minimize

# Definición de la función de beneficio total a maximizar
def beneficio_total(vars):
    x, y = vars
    ingresos = 8*x + 9*y  # Calcula los ingresos totales
    costes = x**2 + y**2 + x*y  # Calcula los costes totales
    return -(ingresos - costes)  # Negativo porque 'minimize' minimiza

# Punto inicial arbitrario
initial_guess = [1, 1]

# Uso de 'minimize' para encontrar el máximo del beneficio total
result = minimize(beneficio_total, initial_guess)

print(f"Cantidad óptima de producto A (x): {result.x[0]}")
print(f"Cantidad óptima de producto B (y): {result.x[1]}")
print(f"Beneficio total máximo: {-result.fun}")

# Explicación del procedimiento
print("""
El procedimiento consiste en definir primero una función de beneficio total que deseamos maximizar. 
Esta función calcula el beneficio total como la diferencia entre los ingresos totales (precio por cantidad vendida) 
y los costes totales (determinados por la función de costes dada). Luego, utilizamos la función 'minimize' de Scipy, 
que busca los valores de 'x' y 'y' que minimizan la función pasada como argumento. 
Dado que queremos maximizar el beneficio total, pasamos el negativo de nuestra función de beneficio para convertir el problema de maximización en uno de minimización.
El punto inicial arbitrario proporciona un lugar de inicio para el algoritmo de búsqueda.
Finalmente, se imprimen los resultados, mostrando las cantidades óptimas de los productos A y B que maximizan el beneficio total de la empresa.""")


#4
def f4(vars): 
    x, y = vars
    return 2*x**2 + 2*x*y + y**2 + 2*x - 3

initial_guess = [0, 0]
result = minimize(f4, initial_guess)

print(f"El punto extremo se encuentra en: {result.x} con un valor de la función de: {result.fun}")

# Explicación
print("""
se utilizó el método de optimización ‘minimize’ con el propósito de encontrar el extremo relativo de la función dada.
     Se inició desde un punto inicial arbitrario de (0, 0). El algoritmo busca el punto en el espacio (x, y) donde la función alcanza 
      un valor extremo (en este caso, mínimo), utilizando el gradiente de la función y otros parámetros internos para guiar la búsqueda 
      hacia el óptimo.""")

#6
def f6(vars):
    x, y, z = vars
    return -x**2 - 5*y**2 + 8*x - 3*z**2 - 10*y + 2*z - 13

initial_guess = [0, 0, 0]
result = minimize(f6, initial_guess)

print(f"El punto extremo se encuentra en: {result.x} con un valor de la función de: {result.fun}")

# Explicación
print("""se aplicó la función ‘minimize’ con el propósito de determinar el punto en el que la función trivariable alcanza su extremo 
      relativo. Se partió desde un punto inicial de [0, 0, 0]. La búsqueda del óptimo se basa en el cálculo del gradiente de la función,
       lo que permite encontrar el punto en el que se minimiza el valor de la función.""")
