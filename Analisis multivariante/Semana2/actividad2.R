# Instalar y cargar el paquete "vegan" si no está instalado
if (!requireNamespace("vegan", quietly = TRUE)) {
  install.packages("vegan")
}
library(vegan)

# Cargar el archivo de datos (asegúrate de reemplazar la ruta con la ubicación real del archivo CSV)
datos <- read.csv("C:/cereal.csv")
print(head(datos)) # Imprimir las primeras filas de los datos

# Verificar si las columnas necesarias están presentes en los datos
required_columns <- c("name", "mfr", "type", "calories", "protein", "fat", "sodium", 
                      "fiber", "carbo", "sugars", "potass", "vitamins", "shelf", 
                      "weight", "cups", "rating")
if (!all(required_columns %in% names(datos))) {
  stop("Algunas columnas necesarias no están presentes en los datos")
}

# Estandarizar las variables numéricas (excluyendo las columnas no numéricas)
numeric_columns <- c("calories", "protein", "fat", "sodium", "fiber", "carbo", 
                     "sugars", "potass", "vitamins", "shelf", "weight", "cups", "rating")
datos[, numeric_columns] <- scale(datos[, numeric_columns])
print(head(datos[, numeric_columns])) # Imprimir las primeras filas de las columnas numéricas estandarizadas

# Calcular la matriz de distancia euclidiana
matriz_distancia <- dist(datos[, numeric_columns])
print(matriz_distancia) # Imprimir la matriz de distancia

# Realizar el escalado multidimensional métrico
escalamiento_metrico <- cmdscale(matriz_distancia, k = 2)
print(escalamiento_metrico) # Imprimir las coordenadas del escalado métrico

# Crear un gráfico bidimensional
plot(escalamiento_metrico, type = "n", xlab = "Dimensión 1", ylab = "Dimensión 2")
sample_indices <- sample(1:nrow(datos), 10)
text(escalamiento_metrico[sample_indices, ], labels = datos$name[sample_indices], cex = 0.7)

# Realizar el escalado multidimensional no métrico utilizando vegan::metaMDS
escalamiento_no_metrico <- metaMDS(matriz_distancia, k = 2)
print(escalamiento_no_metrico) # Imprimir los resultados del escalado no métrico

# Crear un gráfico bidimensional para el escalado no métrico
plot(escalamiento_no_metrico$points, type = "n", xlab = "Dimensión 1", ylab = "Dimensión 2")
sample_indices_no_metrico <- sample(1:nrow(datos), 10)
text(escalamiento_no_metrico$points[sample_indices_no_metrico, ], labels = datos$name[sample_indices_no_metrico], cex = 0.7)

# Obtener la ubicación actual del directorio de trabajo
ubicacion_actual <- getwd()
cat("Ubicación actual del directorio de trabajo:\n")
print(ubicacion_actual) # Imprimir la ubicación actual del directorio de trabajo


