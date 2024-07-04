from scipy.stats import poisson
import numpy as np

# Datos observados
visitas = np.array([300, 350, 950, 400, 370, 75, 725, 80, 380, 375])

# Parámetros de las hipótesis
theta_0 = 330
theta_1 = 480

# Probabilidades previas no informativas
p_prior_0 = 0.5
p_prior_1 = 0.5

# Calculando el logaritmo de la verosimilitud de los datos bajo cada hipótesis
log_likelihood_0 = np.sum(poisson.logpmf(visitas, theta_0))
log_likelihood_1 = np.sum(poisson.logpmf(visitas, theta_1))

# Usando el teorema de Bayes en el espacio logarítmico para evitar underflow
log_evidence = np.logaddexp(log_likelihood_0 + np.log(p_prior_0), log_likelihood_1 + np.log(p_prior_1))
log_posterior_0 = log_likelihood_0 + np.log(p_prior_0) - log_evidence
log_posterior_1 = log_likelihood_1 + np.log(p_prior_1) - log_evidence

# Convirtiendo logaritmos a probabilidades para la salida
p_posterior_0 = np.exp(log_posterior_0)
p_posterior_1 = np.exp(log_posterior_1)

print(f'Probabilidad posterior para H0 (theta = 330): {p_posterior_0}')
print(f'Probabilidad posterior para H1 (theta = 480): {p_posterior_1}')
