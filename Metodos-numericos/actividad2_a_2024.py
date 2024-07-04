import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Definir la matriz de transición
P = np.array([[0.85, 0.05, 0.075],
              [0.05, 0.85, 0.075],
              [0.10, 0.10, 0.85]])

# Dibujar el diagrama de estados
labels = ["A", "B", "C"]
G = nx.DiGraph()

# Añadir nodos y aristas al grafo
for i in range(len(labels)):
    for j in range(len(labels)):
        if P[i, j] > 0:
            G.add_edge(labels[i], labels[j], weight=P[i, j])

pos = nx.spring_layout(G)
edges = G.edges(data=True)

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_weight="bold", arrowsize=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]:.2f}' for u, v, d in edges}, font_size=12)

plt.title("Diagrama de Estados de la Cadena de Markov")
plt.show()
