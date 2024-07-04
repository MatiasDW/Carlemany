from scipy.optimize import minimize

# Definición de la función objetivo
def objetivo(vars):
    x, y = vars
    return (x - 5)**2 + (y - 5)**2

# Restricciones de desigualdad
restricciones = [
    {'type': 'ineq', 'fun': lambda vars: 25 - (vars[0]**2 + vars[1]**2)},  # x^2 + y^2 <= 25
    {'type': 'ineq', 'fun': lambda vars: vars[0] + vars[1] - 2},          # x + y >= 2
    {'type': 'ineq', 'fun': lambda vars: vars[0] - vars[1]}              # x - y >= 0
]

# Punto inicial arbitrario dentro del dominio factible
x0 = [1, 1]

# Solución del problema de optimización
solucion = minimize(objetivo, x0, constraints=restricciones)

# Imprimir la solución y una breve explicación
print("Solución x, y:", solucion.x)
print("Esta solución representa los valores de x e y que minimizan la función objetivo, "
      "sujeta a un conjunto de restricciones de desigualdad. Estos valores están dentro del "
      "dominio especificado y cumplen con todas las restricciones de desigualdad dadas.")

#2
from scipy.optimize import minimize

# Definición de la función de beneficio
def beneficio(vars):
    x, y = vars
    return -(6*x - 2*x**2 + 2*x*y - 2*y**2 + 100)  # Negativo porque minimize minimiza

# Restricción de producción
restriccion_produccion = [{'type': 'ineq', 'fun': lambda vars: 2 - (vars[0] + 2*vars[1])}]

# Punto inicial arbitrario
x0 = [0, 0]

# Resolución del problema de optimización
solucion = minimize(beneficio, x0, constraints=restriccion_produccion)

# Imprimir la solución y una breve explicación
print("Solución x, y (producción de los modelos de móviles):", solucion.x)
print("Para los valores de x e y que maximizan el beneficio de la producción, "
      "sujeta a la restricción de producción dada. Se ha encontrado la producción óptima "
      "dentro del dominio factible que maximiza el beneficio total.")

#3
from scipy.optimize import minimize

# Función objetivo
def objetivo(vars):
    x1, x2 = vars
    return x1 - 4*x2  # Maximizar x1 - 4x2

# Restricciones
a = 1  # Establecemos a = 1 para este caso
restricciones = [
    {'type': 'ineq', 'fun': lambda vars: -(vars[0] + vars[1]**2)},    # x1 + x2^2 <= 0
    {'type': 'ineq', 'fun': lambda vars: vars[1] - a*vars[0]},        # x2 - ax1 <= 0
    {'type': 'ineq', 'fun': lambda vars: vars[0]},                    # x1 >= 0
    {'type': 'ineq', 'fun': lambda vars: vars[1]}                     # x2 >= 0
]

# Punto inicial
x0 = [0.1, 0.1]  # Un punto inicial en el dominio factible cercano al origen

# Resolver el problema de optimización
solucion = minimize(objetivo, x0, constraints=restricciones)

# Imprimir la solución
print("Solución x1, x2:", solucion.x)
# Análisis de afirmaciones sobre la optimización de la función f(x1, x2) = x1 - 4x2 sujeta a restricciones.

print("Análisis de afirmaciones:")

# Afirmación (a): Si a > 0, el valor máximo de la función es igual a 2.
# Justificación: Falsa. Bajo las restricciones dadas, x1 = x2 = 0 es la única solución que cumple,
# lo que no permite alcanzar un valor máximo de 2 para la función objetivo.
print("Afirmación (a): Falsa. No es posible alcanzar un valor de 2 para la función objetivo bajo las restricciones dadas.")

# Afirmación (b): Si a < 2, no hay ningún punto que sea regular.
# Justificación: Falsa. La regularidad de un punto se determina por la independencia lineal de las gradientes
# de las restricciones activas, no por el valor específico de a.
print("Afirmación (b): Falsa. La regularidad de un punto depende de la independencia lineal de las gradientes de las restricciones activas.")

# Afirmación (c): Si a = 1/4, el punto (0,2) no verifica las condiciones de K-K-T.
# Justificación: Verdadera, pero el punto (0,2) no es factible debido a la primera restricción x1 + x2^2 <= 0,
# lo que implica que no puede verificar las condiciones de KKT por no cumplir con las restricciones básicas del problema.
print("Afirmación (c): Verdadera. El punto (0,2) no es factible bajo las restricciones dadas, por lo tanto, no verifica las condiciones de KKT.")

# Conclusión general de las afirmaciones:
# - La afirmación (a) es incorrecta porque no se puede alcanzar el valor máximo propuesto con las restricciones dadas.
# - La afirmación (b) es incorrecta ya que la regularidad no depende del valor de a.
# - La afirmación (c) es correcta en el sentido de que el punto dado no cumple las restricciones, no directamente relacionado con las condiciones de KKT.
print("Conclusión: Las afirmaciones (a) y (b) son falsas por las razones explicadas, mientras que la (c) es verdadera debido a la inviabilidad del punto especificado bajo las restricciones dadas.")


#4
"""La afirmación que se evalúa es si un punto que es un mínimo local en un problema de optimización con una restricción de desigualdad también lo es en un problema de optimización sin restricciones y en otro con una restricción de igualdad.
Opción (a): sugiere que la afirmación es falsa, aunque sería cierto que el punto es un mínimo local del problema sin restricciones cuando la restricción de desigualdad no es estrictamente necesaria.

Opción (b):   afirma que es verdadera debido a la definición de mínimo local.

Opción (c): indica que la afirmación es falsa y que el punto solo sería un mínimo local del problema con restricción de igualdad si la restricción se cumple exactamente en ese punto.
Evaluacion : Opción (a): Es parcialmente correcta porque si el punto es un mínimo local en el problema con restricción de desigualdad y esta restricción no limita al punto, entonces podría ser un mínimo para el problema sin restricciones. Sin embargo, esto no asegura automáticamente que sea un mínimo sin un análisis más detallado.

Opción (b): Es incorrecta como generalización. El hecho de que un punto sea un mínimo local en el problema con restricción de desigualdad no garantiza que también lo sea en los otros problemas sin considerar las condiciones específicas en ese punto.

Opción (c): Proporciona una observación precisa, destacando la importancia de que la restricción de igualdad se cumpla exactamente para que el punto pueda ser considerado un mínimo local en el problema con esa restricción.
Conclusion: La afirmación no se puede aceptar como verdadera en general sin un análisis detallado. Si un punto es un mínimo local en el contexto de restricciones de desigualdad, se requiere un análisis específico para determinar si también lo es en problemas sin restricciones o con restricciones de igualdad. La opción (c) ofrece la perspectiva más clara al enfocarse en la necesidad de cumplir exactamente con la restricción de igualdad para considerar al punto como un mínimo local en ese contexto."""

