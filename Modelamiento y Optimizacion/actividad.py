#1
from sympy import symbols, solve

l, w = symbols('l w')
perimeter = 2 * (l + w) - 2  # La restricción del perímetro
area = l * w  # La función objetivo

# Como el perímetro es 2, resolvemos para una variable en términos de la otra
w_expr = solve(perimeter, w)[0]

# Reemplazamos w en la función del área
area_expr = area.subs(w, w_expr)

# Derivamos la expresión del área respecto a l y encontramos el punto crítico
d_area_dl = area_expr.diff(l)
critical_points = solve(d_area_dl, l)

# Encontramos las dimensiones del rectángulo
dimensions = [(l_val, w_expr.subs(l, l_val)) for l_val in critical_points]
print(f"Dimensiones óptimas para máximo área: {dimensions}")


#2
from scipy.optimize import linprog

# Coeficientes de la función objetivo (costes)
c = [5, 8]  # Costo de cada complejo vitamínico

# Coeficientes de las restricciones de desigualdad (vitaminas A, C, D)
A = [[-2, -3], [-2, -2], [-8, -2]]

# Lado derecho de las restricciones de desigualdad
b = [-36, -28, -32]

# Resolver el problema de programación lineal
res = linprog(c, A_ub=A, b_ub=b, method='highs')

print(f"Combinación de complejos vitamínicos: {res.x}")
print(f"Coste mínimo: {res.fun}")

#3
from sympy import symbols, diff, solve

# Definimos las variables simbólicas
x1, x2, p1, p2 = symbols('x1 x2 p1 p2')

# Definimos la función de coste dada en el problema
C = 2*x1**2 + x1*x2 + 2*x2**2

# Definimos la función de ingreso sin valores específicos para los precios
Ingreso = p1*x1 + p2*x2

# La función de beneficio es la diferencia entre ingreso y coste
Beneficio = Ingreso - C

# Derivamos la función de beneficio respecto a x1 y x2 para encontrar el máximo
derivada_beneficio_x1 = diff(Beneficio, x1)
derivada_beneficio_x2 = diff(Beneficio, x2)

# Igualamos las derivadas a cero para encontrar los puntos críticos
ecuaciones = [derivada_beneficio_x1, derivada_beneficio_x2]
solucion = solve(ecuaciones, (x1, x2))

print(f"Derivada del beneficio respecto a x1: {derivada_beneficio_x1}")
print(f"Derivada del beneficio respecto a x2: {derivada_beneficio_x2}")
print(f"Solución (puntos críticos para x1 y x2): {solucion}")

#4
from scipy.optimize import linprog
import numpy as np

# Coeficientes de la función objetivo (beneficio negativo porque linprog minimiza)
c = [-10, -15]  # Negativo porque queremos maximizar

# Matriz de coeficientes de las restricciones (horas-hombre y horas-máquina)
A = [[4, 7],  # Horas-hombre requeridas por unidad de cada producto
     [3, 6]]  # Horas-máquina requeridas por unidad de cada producto

# Lado derecho de las restricciones (recursos disponibles)
b = [300,  # Horas-hombre disponibles
     500]  # Horas-máquina disponibles

# Límites de las variables (las cantidades producidas no pueden ser negativas)
x0_bounds = (0, None)  # Para el producto 1
x1_bounds = (0, None)  # Para el producto 2

# Resolvemos el problema de programación lineal
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

print(f"Cantidades a producir para maximizar el beneficio: Producto 1: {res.x[0]}, Producto 2: {res.x[1]}")
print(f"Beneficio máximo: {-res.fun}")

#5
print("Esta afirmación es falsa en general. Un máximo local de una función no necesariamente es un máximo global, especialmente en funciones con múltiples picos o valles. Un máximo global es el punto más alto en todo el dominio de la función, mientras que un máximo local es el punto más alto en su vecindad inmediata.")

#6
print("Esta afirmación es verdadera. Un mínimo global, por definición, es el punto más bajo en todo el dominio de la función. Dado que es el punto más bajo, también será un mínimo en su vecindad inmediata, lo que lo convierte en un mínimo local.")

#7
print("Esta afirmación es verdadera. En un conjunto factible convexo, si una función continua es convexa, cualquier mínimo local también es un mínimo global. Dado que la función es convexa, no puede haber múltiples mínimos globales con valores diferentes. Por lo tanto, el valor de la función en todos sus mínimos locales (que también son globales) es el mismo.")

#8
print("Esta afirmación es falsa. La convexidad de una función y su conjunto factible garantiza la existencia de mínimos globales, no máximos. Una función convexa tiende a tener un punto más bajo único (mínimo global) pero no necesariamente un punto más alto único (máximo global).")

#9
print("Esta afirmación es falsa. Una función lineal es un ejemplo de función que es tanto convexa como cóncava al mismo tiempo. En el caso de las funciones lineales, la segunda derivada es cero, lo que satisface tanto la definición de convexidad como la de concavidad.")

#10 a
import matplotlib.pyplot as plt
import numpy as np

# Generamos valores para x e y. Estos valores se utilizan para crear una cuadrícula
# donde se evaluará la función f(x, y) = sqrt(xy) para visualización.
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)  # Creación de la cuadrícula

# Calculamos los valores de Z para cada punto (x, y) en la cuadrícula. Z representa
# los valores de f(x, y) = sqrt(xy), la función cuyos extremos estamos investigando.
Z = np.sqrt(X*Y)

# Creamos una figura para la visualización
plt.figure(figsize=(8, 6))

# Dibujamos las curvas de nivel de f(x, y). Estas curvas muestran cómo cambia el valor
# de la función en el plano xy.
plt.contour(X, Y, Z, levels=20, cmap='RdGy')

# Rellenamos el área que cumple con la restricción y - x <= 0 para ilustrar el conjunto factible.
# Este conjunto incluye todos los puntos (x, y) donde y es menor o igual que x.
plt.fill_between(x, y, y - x, color='lightblue', label='Conjunto factible: y <= x')

# Añadimos leyenda, etiquetas y título para hacer la gráfica más informativa.
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Conjunto Factible y Extremos Relativos de f(x, y) = sqrt(xy)')

# Establecemos límites en los ejes para enfocar la visualización en un área de interés.
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Mostramos la gráfica.
plt.show()

#b
from sympy import symbols, sqrt, diff, solve

# Definimos las variables simbólicas x y y. Estas representan las cantidades
# cuyos valores queremos determinar para maximizar o minimizar la función dada.
x, y = symbols('x y')

# Sustituimos y por -x en la función f(x, y) = sqrt(xy) debido a la restricción y + x = 0.
# Esto nos permite expresar f solo en términos de x, facilitando la derivación.
f = sqrt(x*(-x))

# Derivamos la función f respecto a x para encontrar los puntos donde puede haber extremos.
# Los extremos (máximos o mínimos) de una función ocurren donde su derivada es cero o indefinida.
df_dx = diff(f, x)

# Resolvemos la ecuación derivada igual a cero para encontrar los valores de x
# que satisfacen esta condición. Estos son los puntos críticos de la función.
extremos = solve(df_dx, x)

# Imprimimos los puntos críticos encontrados. Estos puntos son candidatos para ser
# extremos de la función bajo la restricción dada.
print(f"Extremos relativos de f(x, y) sujeto a y + x = 0: {extremos}")

#11
print("Para aplicar el Teorema de Weierstrass, debemos asegurarnos de que el conjunto factible sea cerrado y acotado, y que la función sea continua. La función f(x, y) = 2x - y es continua en todo R^2. Sin embargo, la restricción xy = 2 define una hipérbola, que no es un conjunto cerrado ni acotado. Por lo tanto, no podemos aplicar directamente el Teorema de Weierstrass para garantizar la existencia de un máximo y un mínimo globales.")

#12
print("Para aplicar el Teorema Local-Global en optimización, necesitamos una función convexa o cóncava y un conjunto factible convexo. La función f(x, y) = 2x - y es lineal, y por tanto convexa y cóncava. Sin embargo, la restricción xy = 2 define una hipérbola, que no es un conjunto convexo. Por lo tanto, no se satisfacen completamente las condiciones del teorema para afirmar que todo extremo local es también global.")
