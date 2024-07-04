import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []
test_accuracy = []

# Probar varios modelos con n neighbors-vecinos
neighbors_settings = range(1, 11)
for n_neighbors in neighbors_settings:
    # Construimos el modelo k-NN
    clf = KNeighborsClassifier(n_neighbors = n_neighbors)
    clf.fit(X_train, Y_train)
    # Precision del modelo en datos train
    training_accuracy.append(clf.score(X_train, Y_train))
    # Precision del modelo en datos tes
    test_accuracy.append(clf.score(X_test, Y_test))

    plt.plot(neighbors_settings, training_accuracy, label="Precision con datos train")
    plt.plot(neighbors_settings, test_accuracy, label="Precision con datos test")
    plt.ylabel("Precision del modelo k-NN")
    plt.xlabel("n_neighbors")
    plt.legend()