from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución previa Gamma(α, β)
alpha_prior = 2  # α (forma)
beta_prior = 2   # β (tasa inversa)

# Datos observados: número de llamadas (k) y número de intervalos (n)
k_observed = 10  # k: total de llamadas observadas
n_intervals = 1  # n: número de intervalos de observación, asumiremos 1 para simplificar

# Actualización de parámetros para la distribución posterior Gamma(α', β')
alpha_posterior = alpha_prior + k_observed
beta_posterior = beta_prior + n_intervals

# Crear distribuciones para la visualización
prior_dist = gamma(a=alpha_prior, scale=1/beta_prior)
posterior_dist = gamma(a=alpha_posterior, scale=1/beta_posterior)

# Valores x para la visualización
x = np.linspace(0, 20, 1000)

# Graficar las distribuciones
plt.figure(figsize=(10, 6))
plt.plot(x, prior_dist.pdf(x), label='Distribución Previa (Gamma)')
plt.plot(x, posterior_dist.pdf(x), label='Distribución Posterior (Gamma)', linestyle='--')
plt.title('Actualización Bayesiana: Previa y Posterior')
plt.xlabel('Tasa de Llamadas (λ)')
plt.ylabel('Densidad')
plt.legend()
plt.show()
