from scipy.stats import beta

# Parámetros de la distribución Beta previa
alpha_prior = 4.75
beta_prior = 0.25

# Datos observados
num_successes = 12  # Coches que requirieron reparación
num_failures = 20 - num_successes  # Coches que no requirieron reparación

# Actualizar los parámetros de la distribución posterior Beta
alpha_post = alpha_prior + num_successes
beta_post = beta_prior + num_failures

# Crear una distribución Beta posterior
posterior = beta(alpha_post, beta_post)

# Calcular la media posterior
media_posterior = posterior.mean()

# Calcular la mediana posterior
mediana_posterior = posterior.median()

# Calcular el intervalo de credibilidad del 95%
intervalo_credibilidad = posterior.interval(0.95)

print(f'Media posterior: {media_posterior}')
print(f'Mediana posterior: {mediana_posterior}')
print(f'Intervalo de credibilidad del 95%: {intervalo_credibilidad}')
