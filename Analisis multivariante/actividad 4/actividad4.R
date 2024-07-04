# Instalamos y cargamos los paquetes necesarios
if (!requireNamespace("FactoMineR", quietly = TRUE)) {
  install.packages("FactoMineR")
}
library(FactoMineR)

if (!requireNamespace("cluster", quietly = TRUE)) {
  install.packages("cluster")
}
library(cluster)

if (!requireNamespace("e1071", quietly = TRUE)) {
  install.packages("e1071")
}
library(e1071)

if (!requireNamespace("MVN", quietly = TRUE)) {
  install.packages("MVN")
}
library(MVN)

if (!requireNamespace("biotools", quietly = TRUE)) {
  install.packages("biotools")
}
library(biotools)

# Cargamos los datos
data <- read.table("C:/BreastTissue.txt", header = TRUE, sep = ";", dec = ".")

# Extraemos la columna "Class"
classes <- data$Class
data <- data[, -1]

# Calculamos las distancias Mahalanobis de cada observación a la media
mahalanobis_values <- apply(data, 1, function(x) mahalanobis(x, colMeans(data), cov(data)))

# Imprimimos las primeras 10 distancias Mahalanobis
cat("Primeras 10 Distancias Mahalanobis:\n")
print(mahalanobis_values[1:10])

# Realizamos un resumen estadístico de todas las distancias Mahalanobis
cat("\nResumen Estadístico de las Distancias Mahalanobis:\n")
print(summary(mahalanobis_values))

# Convertimos en una matriz de distancia
mahalanobis_dist <- dist(mahalanobis_values)


# Determinamos el número óptimo de clústeres utilizando el método de la silueta
silhouette_scores <- sapply(2:6, function(k) {
  pam_fit <- pam(as.dist(mahalanobis_dist), k)
  silhouette_widths <- silhouette(pam_fit)
  mean(silhouette_widths[, "sil_width"])
})

# Creamos una tabla con las puntuaciones de silueta
silhouette_table <- data.frame(
  Numero_de_Clusteres = 2:6,
  Puntuacion_Silueta = silhouette_scores
)

# Imprimimos la tabla
print(silhouette_table)

# Identificamos el número óptimo de clústeres
optimal_k <- which.max(silhouette_scores) + 1
cat("\nNúmero óptimo de clústeres:", optimal_k, "\n")


# Realizamos PAM (Partitioning Around Medoids) con el número óptimo de clústeres
pam_fit <- pam(as.dist(mahalanobis_dist), k = optimal_k)
print(pam_fit)

# Realizamos un análisis de componentes principales (PCA)
pca_fit <- PCA(data)
print(pca_fit)

# Realizamos fuzzy clustering
fuzzy_fit <- e1071::cmeans(data, centers = optimal_k, m = 2, iter.max = 500, verbose = TRUE)
print(fuzzy_fit)

# Realizarmos la prueba de normalidad multivariante
mvn_test <- MVN::mvn(data, mvnTest = "mardia")
print(mvn_test)

# Realizamos la prueba de homogeneidad de matrices de covarianza (Box's M) usando el paquete "biotools"
box_m_test <- biotools::boxM(data, classes)

# Efectuamos un resumen de la prueba
print(box_m_test)



