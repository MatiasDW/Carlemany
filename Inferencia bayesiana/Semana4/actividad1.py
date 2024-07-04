import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos del problema
p_prior = stats.beta(4, 75)  # Distribución Beta (4, 75) para la creencia inicial
data = np.array([1] * 12 + [0] * 8)  # 12 coches requieren reparación, 8 no

# A) Cálculos exactos
posterior_exacta = stats.beta(p_prior.a + sum(data), p_prior.b + len(data) - sum(data))

# Media posterior
media_posterior_exacta = posterior_exacta.mean()

# Mediana posterior
mediana_posterior_exacta = posterior_exacta.median()

# Intervalo de credibilidad del 95%
intervalo_credibilidad_exacto = posterior_exacta.interval(0.95)

# Visualización de la distribución posterior exacta
x_exacta = np.linspace(0, 1, 1000)
y_exacta = posterior_exacta.pdf(x_exacta)

plt.plot(x_exacta, y_exacta, label='Distribución Posterior Exacta')
plt.title('Distribución Posterior - Cálculos Exactos')
plt.xlabel('Probabilidad de Requiere Reparación')
plt.ylabel('Densidad de Probabilidad')
plt.axvline(media_posterior_exacta, color='r', linestyle='--', label='Media Posterior')
plt.axvline(mediana_posterior_exacta, color='g', linestyle='--', label='Mediana Posterior')
plt.fill_between(x_exacta, y_exacta, where=[(a >= intervalo_credibilidad_exacto[0]) and (a <= intervalo_credibilidad_exacto[1]) for a in x_exacta], alpha=0.3, label='Intervalo Credibilidad (95%)')
plt.legend()
plt.show()

# Imprime los resultados exactos
print("Resultados con cálculos exactos:")
print(f"Media Posterior (exacta): {media_posterior_exacta:.4f}")
print(f"Mediana Posterior (exacta): {mediana_posterior_exacta:.4f}")
print(f"Intervalo de Credibilidad del 95% (exacto): {intervalo_credibilidad_exacto}\n")

# B) Simulaciones de Monte Carlo con diferentes tamaños de muestra
tamanos_muestra = [30, 3000, 30000]

for N in tamanos_muestra:
    muestras = np.random.choice(data, size=(N, len(data)), replace=True)
    proporciones = muestras.mean(axis=1)

    # Visualización de las simulaciones de Monte Carlo
    plt.hist(proporciones, bins=30, alpha=0.5, label=f'MC - N={N}')

    # Imprime los resultados de las simulaciones
    print(f"Resultados con simulación de Monte Carlo (N={N}):")
    print(f"Media Posterior (MC): {proporciones.mean():.4f}")
    print(f"Mediana Posterior (MC): {np.median(proporciones):.4f}")
    print(f"Intervalo de Credibilidad del 95% (MC): {np.percentile(proporciones, [2.5, 97.5])}\n")

plt.title('Simulaciones de Monte Carlo')
plt.xlabel('Probabilidad de Requiere Reparación')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
