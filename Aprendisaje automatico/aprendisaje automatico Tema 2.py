# Importar la función para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split

# Dividir el conjunto de datos en datos de entrenamiento y prueba de manera aleatoria
X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

# Importar la clase del modelo k-NN
from sklearn.neighbors import KNeighborsClassifier

# Crear una instancia del clasificador k-NN con un vecino cercano (n_neighbors=1)
knn = KNeighborsClassifier(n_neighbors=1)

# Entrenar el modelo k-NN en el conjunto de entrenamiento
knn.fit(X_train, Y_train)

# Evaluar el rendimiento del modelo en el conjunto de prueba y mostrar la precisión
score = knn.score(X_test, Y_test)
print("Score del test: {:2f}".format(score))
