import numpy as np
from scipy.stats import poisson, chi2
import matplotlib.pyplot as plt

data = np.array([300, 350, 950, 400, 370, 75, 725, 80, 380, 375])

# Estimador de máxima verosimilitud
theta_hat = np.mean(data)

# Estadístico de prueba de razón de verosimilitudes
D = -2 * np.sum(poisson.logpmf(data, mu=theta_hat) - poisson.logpmf(data, mu=330))
p_value = 1 - chi2.cdf(D, df=1)

print(f"P-valor para la prueba de razón de verosimilitudes: {p_value}")

# Histograma de las visitas
plt.hist(data, bins=20, alpha=0.7, label='Visitas')

# Líneas para mostrar los valores de theta y theta_hat
plt.axvline(330, color='red', linestyle='dashed', linewidth=2, label=r'$\theta$')
plt.axvline(theta_hat, color='green', linestyle='dashed', linewidth=2, label=r'$\hat{\theta}$')

plt.legend()
plt.title('Distribución de Visitas y Parámetros')
plt.xlabel('Número de Visitas')
plt.ylabel('Frecuencia')
plt.show()
