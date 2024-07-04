from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, Y_train)

print("Precision en datos entrenamiento: {:.3f}".format(tree.score(X_train, Y_train)))
print("Precision en datos de test: {:.3f}".format(tree.score(X_test, Y_test)))

precision en datos entrenamiento: 1.000
precision en datos de test: 0.937

tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, Y_train)
print("Precision en datos entrenamiento: {:.3f}".format(tree.score(X_train, Y_train)))
print("Precision en datos de test: {:.3f}".format(tree.score(X_test, Y_test)))

precision en datos entrenamiento: 0.988
precision en datos de test: 0.951

from sklearn.tree import export_graphviz

export_graphviz(tree, out_file="tree.dot", class_names=["malignant", "bening"],
feature_names=cancer.feature_names, impurity=False, filled=True)
import graphviz
with open("tree.dot") as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)

import matplotlib.pyplot as plt

def plot_features_importances_cancer(model):
    n_features = cancer.data.shape[1]
    plt.brah(range(n_features), model.feature_importances_, align="center")
    plt.yticks(np.arange(n_features), cancer.feature_names)
    plt.xlabel("Importancia de la caracteristica")
    plt.ylabel("Caracteristica")

plot_features_importances_cancer(tree)