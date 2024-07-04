import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
yt = [28, 27.6, 28, 34.4, 45.5, 45.5, 41, 26.9, 26.2, 30.1]
metodo_a = [None, 27.1, 28.5, 33.5, 44.8, 46, 40.6, 27.2, 27, 29.5]
metodo_b = [None, 28, 27.8, 28.1, 35.7, 36.9, 37.9, 38.1, 37.1, 35]
# Aseguramos que solo se tomen en cuenta los años en que ambos métodos hicieron predicciones
yt = yt[1:]
metodo_a = metodo_a[1:]
metodo_b = metodo_b[1:]
# Calcular errores absolutos y cuadráticos para cada año desde 2004 hasta 2012
errores_absolutos_a = [abs(a - y) for a, y in zip(metodo_a, yt)]
errores_absolutos_b = [abs(b - y) for b, y in zip(metodo_b, yt)]
errores_cuadraticos_a = [(a - y)**2 for a, y in zip(metodo_a, yt)]
errores_cuadraticos_b = [(b - y)**2 for b, y in zip(metodo_b, yt)]
# Calcular MAE y MSE para cada método
mae_a = np.mean(errores_absolutos_a)
mae_b = np.mean(errores_absolutos_b)
mse_a = np.mean(errores_cuadraticos_a)
mse_b = np.mean(errores_cuadraticos_b)
print("MAE del Método A: ", mae_a)
print("MAE del Método B: ", mae_b)
print("MSE del Método A: ", mse_a)
print("MSE del Método B: ", mse_b)
# Para los gráficos
years = list(range(2004, 2013))
plt.figure(figsize=(12, 6))
# Serie original y Método A
plt.subplot(1, 2, 1)
plt.plot(years, yt, label='Serie Original')
plt.plot(years, metodo_a, label='Método A')
plt.legend()
plt.title('Serie Original vs Método A')
plt.xlabel('Años')
plt.ylabel('Valores')
# Serie original y Método B
plt.subplot(1, 2, 2)
plt.plot(years, yt, label='Serie Original')
plt.plot(years, metodo_b, label='Método B')
plt.legend()
plt.title('Serie Original vs Método B')
plt.xlabel('Años')
plt.ylabel('Valores')
plt.tight_layout()
plt.show()
