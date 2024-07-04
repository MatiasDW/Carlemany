import numpy as np
from scipy.stats import gamma
from scipy.stats import beta

# Supongamos que tenemos los siguientes parámetros para la distribución previa Gamma
a_prior = 1  # Parámetro 'a' de la distribución Gamma
b_prior = 1  # Parámetro 'b' de la distribución Gamma

# Datos observados
data = np.array([2, 3, 4])  # Aquí deberías ingresar tus datos observados

# Cálculo de los parámetros de la distribución posterior
a_post = a_prior + len(data)
b_post = b_prior + np.sum(data)

# Crear una distribución Gamma posterior
posterior = gamma(a=a_post, scale=1/b_post)

# Imprimir los parámetros actualizados de la distribución posterior
print(f'Parámetros de la distribución Gamma posterior: a={a_post}, b={b_post}')

#1A.2
# Parámetros de la distribución Beta previa
a_prior = 1  # Parámetro 'a' de la distribución Beta
b_prior = 1  # Parámetro 'b' de la distribución Beta

# Datos observados
data = np.array([1, 0, 2, 1])  # Aquí debes ingresar tus datos observados para y_i

# Cálculo de los parámetros de la distribución posterior
a_post = a_prior + np.sum(data)
b_post = b_prior + len(data)

# Crear una distribución Beta posterior
posterior = beta(a=a_post, b=b_post)

# Imprimir los parámetros actualizados de la distribución posterior
print(f'Parámetros de la distribución Beta posterior: a={a_post}, b={b_post}')
