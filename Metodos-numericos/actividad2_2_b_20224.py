import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición
P = np.array([[0.50, 0.30, 0],
              [0, 0.60, 0.40],
              [2, 0, 0.90]])

# Definir la distribución inicial
initial_distribution = np.array([100, 50, 20])

# Aplicar la matriz de transición cuatro veces
distribution_after_four_months = np.linalg.matrix_power(P, 4).dot(initial_distribution)

# Graficar la distribución inicial y final
labels = ['Plántula', 'Planta Joven', 'Planta Adulta']
x = np.arange(len(labels))

fig, ax = plt.subplots()
bar_width = 0.35

bars1 = ax.bar(x - bar_width/2, initial_distribution, bar_width, label='Inicial')
bars2 = ax.bar(x + bar_width/2, distribution_after_four_months, bar_width, label='Final')

ax.set_xlabel('Estados')
ax.set_ylabel('Cantidad')
ax.set_title('Distribución de Plantas Inicial y Final')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')  # agregar valores encima de las barras

for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')  # agregar valores encima de las barras

plt.show()

distribution_after_four_months
