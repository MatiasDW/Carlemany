import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición
P = np.array([[0.85, 0.05, 0.075],
              [0.05, 0.85, 0.075],
              [0.10, 0.10, 0.85]])

# Definir la distribución inicial
initial_distribution = np.array([0.60, 0.20, 0.20])

# Aplicar la matriz de transición tres veces
distribution_after_three_campaigns = np.linalg.matrix_power(P, 3).dot(initial_distribution)

# Calcular la variación porcentual para A
initial_A = initial_distribution[0]
final_A = distribution_after_three_campaigns[0]
percentage_change_A = ((final_A - initial_A) / initial_A) * 100

# Graficar la distribución inicial y final
labels = ['A', 'B', 'C']
x = np.arange(len(labels))

fig, ax = plt.subplots()
bar_width = 0.35

bars1 = ax.bar(x - bar_width/2, initial_distribution, bar_width, label='Inicial')
bars2 = ax.bar(x + bar_width/2, distribution_after_three_campaigns, bar_width, label='Final')

ax.set_xlabel('Compañías')
ax.set_ylabel('Distribución')
ax.set_title('Distribución de Usuarios Inicial y Final')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')  # agregar valores encima de las barras

for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')  # agregar valores encima de las barras

plt.show()

percentage_change_A
