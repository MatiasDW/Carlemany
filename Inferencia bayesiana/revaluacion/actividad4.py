# Parámetros de la distribución previa Beta
alpha_prior = 2
beta_prior = 2

# Número de éxitos y fracasos observados
num_successes = 10
num_failures = 5

# Actualizar parámetros de la distribución posterior Beta
alpha_post = alpha_prior + num_successes
beta_post = beta_prior + num_failures

# Probabilidad predictiva posterior para y* = 0
p_y_star_0 = beta_post / (alpha_post + beta_post)

print(f'Probabilidad predictiva posterior para y* = 0: {p_y_star_0}')
