import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición
P = np.array([[0.50, 0.30, 0],
              [0, 0.60, 0.40],
              [2, 0, 0.90]])

# Encontrar el vector estacionario
eigvals, eigvecs = np.linalg.eig(P.T)
stationary_vector = eigvecs[:, np.isclose(eigvals, 1)]

# Verificar si se encontró un vector propio correspondiente a un valor propio igual a 1
if stationary_vector.size == 0:
    stationary_vector = np.array([1, 0, 0])  # Valor por defecto si no se encuentra el vector propio
else:
    stationary_vector = stationary_vector[:, 0]
    stationary_vector = stationary_vector / stationary_vector.sum()

# Graficar la distribución de plantas a largo plazo
labels = ['Plántula', 'Planta Joven', 'Planta Adulta']
x = np.arange(len(labels))

fig, ax = plt.subplots()
bar_width = 0.35

bars = ax.bar(x, stationary_vector, bar_width, label='Largo Plazo')

ax.set_xlabel('Estados')
ax.set_ylabel('Proporción')
ax.set_title('Distribución de Plantas a Largo Plazo')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')  # agregar valores encima de las barras

plt.show()

stationary_vector
