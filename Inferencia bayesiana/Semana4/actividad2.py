import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos del problema
observed_data = np.array([1.54, 1.60, 1.56, 1.81, 1.91, 1.68, 1.76, 1.85, 1.69, 1.65])
prior_theta = stats.norm(loc=1.8, scale=0.25)
prior_sigma2 = stats.invgamma(a=0.02, scale=1)

# Muestreador de Gibbs
def gibbs_sampler(data, iterations):
    samples_theta = []
    samples_sigma2 = []

    theta = prior_theta.rvs()
    sigma2 = prior_sigma2.rvs()

    for _ in range(iterations):
        # Distribución condicional de theta
        theta = np.random.normal(np.mean(data), np.sqrt(sigma2 / len(data)))

        # Distribución condicional de sigma^2
        sigma2 = stats.invgamma.rvs(a=len(data) / 2, scale=np.sum((data - theta) ** 2) / 2)

        samples_theta.append(theta)
        samples_sigma2.append(sigma2)

    return np.array(samples_theta), np.array(samples_sigma2)

# Genera 10,000 simulaciones
iterations = 10000
theta_samples, sigma2_samples = gibbs_sampler(observed_data, iterations)

# Visualización de las simulaciones
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(theta_samples, label='Simulaciones de Theta')
plt.title('Simulaciones de Theta')
plt.xlabel('Iteraciones')
plt.ylabel('Valor de Theta')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(sigma2_samples, label='Simulaciones de Sigma^2', color='orange')
plt.title('Simulaciones de Sigma^2')
plt.xlabel('Iteraciones')
plt.ylabel('Valor de Sigma^2')
plt.legend()

plt.show()

print(f"Resultados de Simulaciones de Theta:")
print(f"Media de Theta: {np.mean(theta_samples):.4f}")
print(f"Mediana de Theta: {np.median(theta_samples):.4f}")
print(f"Intervalo de Credibilidad del 95% de Theta: [{np.percentile(theta_samples, 2.5):.4f}, {np.percentile(theta_samples, 97.5):.4f}]")
print("\nResultados de Simulaciones de Sigma^2:")
print(f"Media de Sigma^2: {np.mean(sigma2_samples):.4f}")
print(f"Mediana de Sigma^2: {np.median(sigma2_samples):.4f}")
print(f"Intervalo de Credibilidad del 95% de Sigma^2: [{np.percentile(sigma2_samples, 2.5):.4f}, {np.percentile(sigma2_samples, 97.5):.4f}]")
