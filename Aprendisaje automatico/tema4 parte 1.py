import numpy as np
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

print("cancer.keys(): \n{}" .format(cancer.keys()))
print("Datos en la base de datos tumores: {}" .format(cancer.data.shape))
print("Numero de instancias de cada tipo tumor o etiquetas: \n{}" .format({n: v for n, v in zip(cancer.target_name, np.bicount(cancer.target))}))
print("Carecteristicas de cada tumor: \n{}" .format(cancer.feature_names))

cancer.keys():
dict_keys(["data", "target", "frame", "target_names", "DESCR", "features_names", "filename", "data_module"])
Datos en la base de datos de tumores: (569, 30)
Numero de instancias de cada tipo de tumor o etiquetas:
{"malignant": 212, "benign": 357}
Caracterisicas de cada tumor:
["mean radius" "mean texture" "mean perimeter" "mean area" "mean smoothness" "mean compactness" "mean concavity"
 " mean concave points" "mean symmetry" "mean fractal dimension" "radius error" "texture error" "perimeter error" "area error"
 "smoothness error" "compactness error" "concavity error" "concave points error" "symmetry error" "fractal dimension error"
 "worst radius" "worst texture" "worst perimeter" "worst area" "worst smoothness" "worst compactness" "worst concavity" "worst concave points"
 "worst symmetry" "worst fractal dimension"]