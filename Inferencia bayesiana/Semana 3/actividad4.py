import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma, poisson

# Datos de la muestra
data = np.array([5, 8, 12, 6, 10, 7, 9, 11, 4, 8])

# Parámetros previos no informativos
alpha_prior = 1
beta_prior = 1

# Parámetros de la distribución predictiva posterior
alpha_post = alpha_prior + np.sum(data)
beta_post = beta_prior + len(data)

# Generar valores para la distribución predictiva posterior
x = np.arange(0, 25)
posterior_predictive = poisson.pmf(x, alpha_post)

# Imprimir resultados
print(f'Parámetros previos: alpha = {alpha_prior}, beta = {beta_prior}')
print(f'Parámetros posteriores: alpha = {alpha_post}, beta = {beta_post}')

# Calcular la probabilidad de y* = 0
prob_y_star_0 = poisson.pmf(0, alpha_post)
print(f'Probabilidad de y* = 0: {prob_y_star_0}')

# Graficar la distribución predictiva posterior
plt.bar(x, posterior_predictive, label='Distribución Predictiva Posterior', alpha=0.7)
plt.title('Distribución Predictiva Posterior del Modelo Gamma-Poisson')
plt.xlabel('Número de Eventos')
plt.ylabel('Probabilidad')
plt.legend()
plt.show()
