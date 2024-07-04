from scipy.optimize import minimize
import numpy as np

# Definición de la función objetivo
def funcion_objetivo(vars):
    x, y = vars
    return 3*x**2 + x*y + 4*y**2 - 6*x

# Definición de la restricción
def restriccion(vars):
    x, y = vars
    return 3*x + y - 6

# Condiciones iniciales arbitrarias
x0 = [0, 0]

# Restricción en formato requerido por scipy.optimize
cons = ({'type': 'eq', 'fun': restriccion})

# Solución usando scipy.optimize.minimize
sol = minimize(funcion_objetivo, x0, method='SLSQP', constraints=cons)

print("Solución x, y:", sol.x)


#3
from scipy.optimize import minimize
import numpy as np

# Definición de la función de beneficio a maximizar
def funcion_beneficio(vars):
    x, y, z = vars
    ingresos = 86*x + 88*y + 26*z
    costes = x**2 + y**2 + z**2 + 2*x*y
    return -(ingresos - costes)  # Minimizamos el negativo del beneficio para maximizar el beneficio

# Definición de la restricción de producción
def restriccion_produccion(vars):
    x, y, z = vars
    return x + 2*y + 3*z - 90

# Condiciones iniciales arbitrarias
x0 = [0, 0, 0]

# Restricción en formato requerido por scipy.optimize
cons_produccion = ({'type': 'eq', 'fun': restriccion_produccion})

# Solución usando scipy.optimize.minimize
sol_produccion = minimize(funcion_beneficio, x0, method='SLSQP', constraints=cons_produccion)

print("Producción optimizada x, y, z:", sol_produccion.x)
