import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición
P = np.array([[0.85, 0.05, 0.075],
              [0.05, 0.85, 0.075],
              [0.10, 0.10, 0.85]])

# Encontrar el vector estacionario
eigvals, eigvecs = np.linalg.eig(P.T)
stationary_vector = eigvecs[:, np.isclose(eigvals, 1)]
stationary_vector = stationary_vector[:, 0]
stationary_vector = stationary_vector / stationary_vector.sum()

# Graficar la distribución a largo plazo
labels = ['A', 'B', 'C']
x = np.arange(len(labels))

fig, ax = plt.subplots()
bar_width = 0.35

bars = ax.bar(x, stationary_vector, bar_width, label='Largo Plazo')

ax.set_xlabel('Compañías')
ax.set_ylabel('Distribución')
ax.set_title('Distribución de Usuarios a Largo Plazo')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')  # agregar valores encima de las barras

plt.show()

stationary_vector
