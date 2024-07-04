import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, bernoulli

# Datos de la muestra
data = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1])

# Parámetros previos no informativos
alpha_prior = 1
beta_prior = 1

# Parámetros de la distribución predictiva posterior
alpha_post = alpha_prior + np.sum(data)
beta_post = beta_prior + len(data) - np.sum(data)

# Generar valores para la distribución predictiva posterior
x = np.linspace(0, 1, 1000)
posterior_predictive = beta.pdf(x, alpha_post, beta_post)

# Imprimir resultados
print(f'Parámetros previos: alpha = {alpha_prior}, beta = {beta_prior}')
print(f'Parámetros posteriores: alpha = {alpha_post}, beta = {beta_post}')

# Calcular la probabilidad de y* = 0
prob_y_star_0 = beta.cdf(0, alpha_post, beta_post)
print(f'Probabilidad de y* = 0: {prob_y_star_0}')

# Graficar la distribución predictiva posterior
plt.plot(x, posterior_predictive, label='Distribución Predictiva Posterior')
plt.title('Distribución Predictiva Posterior del modelo Bernoulli-Beta')
plt.xlabel('Probabilidad')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()
