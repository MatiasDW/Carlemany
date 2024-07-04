import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos de la Actividad 1
datos_actividad_1 = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                              2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5])

# Distribución previa
prior_alpha = 2
prior_beta = 1

# Distribución posterior bajo modelo Poisson
posterior_alpha = prior_alpha + np.sum(datos_actividad_1)
posterior_beta = prior_beta + len(datos_actividad_1)

# Estimadores bayesianos
estimador_cuadratico = posterior_alpha / (posterior_alpha + posterior_beta)
estimador_lineal = (posterior_alpha + 1) / (posterior_alpha + posterior_beta + 2)
estimador_discreto = (posterior_alpha + 0.5) / (posterior_alpha + posterior_beta + 1)

# Intervalo bayesiano de credibilidad al 95%
intervalo_credibilidad = stats.beta.interval(0.95, posterior_alpha, posterior_beta)

# Resultados
print("Distribución posterior bajo modelo Poisson:")
print(f"Alpha: {posterior_alpha}, Beta: {posterior_beta}")
print("\nEstimadores bayesianos:")
print(f"Cuadrático: {estimador_cuadratico}")
print(f"Lineal: {estimador_lineal}")
print(f"Discreto: {estimador_discreto}")
print("\nIntervalo de credibilidad al 95%:", intervalo_credibilidad)


# Generar muestras para graficar las distribuciones
x = np.linspace(0, 1, 1000)
prior_dist = stats.beta(prior_alpha, prior_beta).pdf(x)
posterior_dist = stats.beta(posterior_alpha, posterior_beta).pdf(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, prior_dist, label='Distribución Previa', linestyle='--')
plt.plot(x, posterior_dist, label='Distribución Posterior', linestyle='-')
plt.title('Distribución Previa y Posterior bajo Modelo Poisson')
plt.xlabel('Parámetro θ')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()

# Actividad 2
# Datos
error_anterior = 0.17
tamano_muestra = 100
fallos_nuevo_metodo = 12

# Distribución previa
prior_a = 1
prior_b = 6

# Distribución posterior bajo modelo Binomial
posterior_a = prior_a + fallos_nuevo_metodo
posterior_b = prior_b + (tamano_muestra - fallos_nuevo_metodo)

# Estimadores bayesianos
estimador_cuadratico_2 = posterior_a / (posterior_a + posterior_b)
estimador_lineal_2 = (posterior_a + 1) / (posterior_a + posterior_b + 2)
estimador_discreto_2 = (posterior_a + 0.5) / (posterior_a + posterior_b + 1)

# Intervalo bayesiano de credibilidad al 95%
intervalo_credibilidad_2 = stats.beta.interval(0.95, posterior_a, posterior_b)

# Resultados
print("Actividad 2:")
print("Distribución posterior bajo modelo Binomial:")
print(f"Alpha: {posterior_a}, Beta: {posterior_b}")
print("\nEstimadores bayesianos:")
print(f"Cuadrático: {estimador_cuadratico_2}")
print(f"Lineal: {estimador_lineal_2}")
print(f"Discreto: {estimador_discreto_2}")
print("\nIntervalo de credibilidad al 95%:", intervalo_credibilidad_2)
print("\n-----------------------------------------------------")

# Generar muestras para graficar las distribuciones
x = np.linspace(0, 1, 1000)
prior_dist_2 = stats.beta(prior_a, prior_b).pdf(x)
posterior_dist_2 = stats.beta(posterior_a, posterior_b).pdf(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, prior_dist_2, label='Distribución Previa', linestyle='--')
plt.plot(x, posterior_dist_2, label='Distribución Posterior', linestyle='-')
plt.title('Distribución Previa y Posterior bajo Modelo Binomial')
plt.xlabel('Parámetro θ')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()

# Actividad 3
# Datos
clientes_totales = 15000
tamaño_muestra_actividad_3 = 50
reclamaciones_falsas = 0
media_esperada = 0.05
moda_esperada = 0.03

# Estimación de hiperparámetros a y b
a = ((1 - media_esperada) / (media_esperada - moda_esperada**2)) * (moda_esperada**2)
b = a * ((1 / moda_esperada) - 1)

# Distribución posterior bajo modelo Beta
posterior_a_3 = a + reclamaciones_falsas
posterior_b_3 = b + tamaño_muestra_actividad_3 - reclamaciones_falsas

# Estimadores puntuales del parámetro 𝜃
estimador_1 = (posterior_a_3) / (posterior_a_3 + posterior_b_3)
estimador_2 = (posterior_a_3 + 1) / (posterior_a_3 + posterior_b_3 + 2)

# Intervalo bayesiano de credibilidad al 95%
intervalo_credibilidad_3 = stats.beta.interval(0.95, posterior_a_3, posterior_b_3)

# Resultados
print("Actividad 3:")
print("Hiperparámetros a y b:")
print(f"a: {a}, b: {b}")
print("\nDistribución posterior bajo modelo Beta:")
print(f"Alpha: {posterior_a_3}, Beta: {posterior_b_3}")
print("\nEstimadores puntuales del parámetro 𝜃:")
print(f"Estimador 1: {estimador_1}")
print(f"Estimador 2: {estimador_2}")
print("\nIntervalo de credibilidad al 95%:", intervalo_credibilidad_3)
print("\n-----------------------------------------------------")

# Generar muestras para graficar las distribuciones
x = np.linspace(0, 1, 1000)
prior_dist_3 = stats.beta(a, b).pdf(x)
posterior_dist_3 = stats.beta(posterior_a_3, posterior_b_3).pdf(x)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, prior_dist_3, label='Distribución Previa', linestyle='--')
plt.plot(x, posterior_dist_3, label='Distribución Posterior', linestyle='-')
plt.title('Distribución Previa y Posterior bajo Modelo Beta')
plt.xlabel('Parámetro θ')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()

# Actividad 4

respuesta_pregunta_teorica = """
La principal diferencia entre la interpretación de un intervalo de confianza frecuentista 
y un intervalo de credibilidad bayesiano radica en la naturaleza de las afirmaciones 
hechas sobre el parámetro de interés.

En el enfoque frecuentista, el intervalo de confianza se interpreta de la siguiente manera: 
si repitiéramos el experimento un número infinito de veces, el 95% de los intervalos de 
confianza construidos contendrían el verdadero valor del parámetro. Aquí, el parámetro es 
considerado fijo y el intervalo es variable.

Por otro lado, en el enfoque bayesiano, el intervalo de credibilidad se interpreta como la 
probabilidad de que el parámetro esté dentro del intervalo dada la información observada y 
la distribución previa. Es decir, se proporciona una medida directa de la creencia en la 
presencia del parámetro en el intervalo. Aquí, el intervalo es fijo y el parámetro es 
considerado como una variable aleatoria.

En resumen, la diferencia clave radica en la interpretación probabilística directa en el 
enfoque bayesiano, mientras que el enfoque frecuentista se basa en propiedades de 
repetición de muestreo a largo plazo.
"""

# Resultados
print("Actividad 4:")
print("Respuesta a la pregunta teórica:")
print(respuesta_pregunta_teorica)

