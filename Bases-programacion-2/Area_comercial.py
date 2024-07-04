import numpy as np

def calcular_comisiones_y_promedios(m, target_anual):
    # Create matrix to store [ID, average_sales, commissions]
    resultados = []
    
    # Calculate the monthly target
    target_mensual = target_anual / 12
    
    for fila in m:
        id_empleado = fila[0]
        ventas = np.array(fila[1:], dtype=float)
        average_sales = np.mean(ventas)
        total_sales = np.sum(ventas)
        
        # Calculate commissions
        if average_sales < 0.7 * target_mensual:
            commissions = 0
        elif average_sales < 1.15 * target_mensual:
            commissions = 0.004 * total_sales
        else:
            commissions = 0.006 * total_sales
        
        resultados.append([id_empleado, average_sales, commissions])
    
    return np.array(resultados, dtype=object)

def mejor_y_peor_vendedor(resultados):
    # Convert results to a numpy array for easier handling
    resultados = np.array(resultados, dtype=object)
    
    # Find best and worst seller
    best_seller = resultados[np.argmax(resultados[:, 2])]
    worst_seller = resultados[np.argmin(resultados[:, 2])]
    
    return best_seller, worst_seller

def mejor_mes_venta(m):
    # Sum sales for each month
    sales_per_month = np.sum(np.array(m)[:, 1:], axis=0)
    
    # Find the index of the best month
    best_month = np.argmax(sales_per_month)
    
    return best_month + 1  # +1 because months are usually numbered from 1

# Example usage
m = [
    ["1", 100, 150, 200],
    ["2", 50, 60, 70],
    ["3", 300, 350, 400],
]
target_anual = 1200

resultados = calcular_comisiones_y_promedios(m, target_anual)
mejor_vendedor, peor_vendedor = mejor_y_peor_vendedor(resultados)
mejor_mes = mejor_mes_venta(m)

print("Best Seller:", mejor_vendedor)
print("Worst Seller:", peor_vendedor)
print("Best Sales Month:", mejor_mes)
