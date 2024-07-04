import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt

# Datos de ejemplo
y = np.random.normal(20, 1, 20)

# Funciones de verosimilitud bajo ambas hipótesis
L_sigma1 = np.prod(norm.pdf(y, loc=20, scale=1))
L_sigma3 = np.prod(norm.pdf(y, loc=20, scale=np.sqrt(3)))

# Bayes Factor
BF_10 = L_sigma1 / L_sigma3

print(f"Bayes Factor B10: {BF_10}")

# Gráfico de observaciones y distribuciones normales
sns.histplot(y, kde=True, label='Observaciones', color='blue')

# Distribuciones normales bajo ambas hipótesis
x = np.linspace(15, 25, 100)
plt.plot(x, norm.pdf(x, loc=20, scale=1), label=r'$\sigma^2=1$', color='red')
plt.plot(x, norm.pdf(x, loc=20, scale=np.sqrt(3)), label=r'$\sigma^2=3$', color='green')

plt.title('Distribución de Observaciones y Modelos')
plt.xlabel('Observaciones')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()
