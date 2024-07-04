from scipy.stats import gamma
import numpy as np

# Datos observados
data = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5])

# Parámetros de la distribución previa Gamma
alpha_prior = 2
beta_prior = 1

# Cálculo de los parámetros de la distribución posterior Gamma
alpha_post = alpha_prior + np.sum(data)
beta_post = beta_prior + len(data)

# Distribución posterior Gamma
posterior = gamma(alpha_post, scale=1/beta_post)

print(f'Parámetros de la distribución Gamma posterior: alpha={alpha_post}, beta={beta_post}')

#2b y 2C
from scipy.stats import gamma

# Parámetros de la distribución Gamma posterior
alpha_post = 105
beta_post = 51

# Crear una distribución Gamma posterior
posterior = gamma(alpha_post, scale=1/beta_post)

# Estimadores bayesianos para diferentes funciones de riesgo
estimador_media = posterior.mean()
estimador_moda = (alpha_post - 1) / beta_post  # Modo para alpha > 1
# La mediana de la distribución Gamma no tiene una solución analítica sencilla
# y se obtiene numéricamente.
estimador_mediana = posterior.median()

print(f'Estimador bayesiano para la función de riesgo cuadrática (media): {estimador_media}')
print(f'Estimador bayesiano para la función de riesgo discreta (modo): {estimador_moda}')
print(f'Estimador bayesiano para la función de riesgo lineal (mediana): {estimador_mediana}')

# Intervalo de credibilidad del 95%
intervalo_credibilidad = posterior.interval(0.95)
print(f'Intervalo bayesiano de credibilidad del 95%: {intervalo_credibilidad}')

