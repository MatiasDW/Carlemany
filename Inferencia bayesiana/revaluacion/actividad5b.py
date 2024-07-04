import numpy as np
from scipy.stats import beta

# Parámetros de la distribución posterior Beta
alpha_post = 16.75  # alpha_prior + número de éxitos
beta_post = 8.25    # beta_prior + número de fracasos

# Tamaños de muestra para las simulaciones de Monte Carlo
sample_sizes = [30, 3000, 30000]

# Realizar simulaciones de Monte Carlo y calcular estadísticas
for size in sample_sizes:
    # Generar muestras de la distribución posterior
    samples = beta.rvs(alpha_post, beta_post, size=size)

    # Calcular la media, la mediana y el intervalo de credibilidad del 95%
    sample_mean = np.mean(samples)
    sample_median = np.median(samples)
    credibility_interval = np.percentile(samples, [2.5, 97.5])

    # Mostrar los resultados
    print(f'\nTamaño de muestra: {size}')
    print(f'Media estimada por Monte Carlo: {sample_mean}')
    print(f'Mediana estimada por Monte Carlo: {sample_median}')
    print(f'Intervalo de credibilidad del 95% estimado por Monte Carlo: {credibility_interval}')
