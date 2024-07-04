from collections import deque

def comprobarPasoPieza(elemento, numeroReceta):
    # Check if all values in the element are zero
    if all(x == 0 for x in elemento):
        print(f"La receta {numeroReceta} está a cero.")
        return False
    
    # Check Prensa -> Transportador
    if elemento[0] != elemento[1]:
        print(f"La receta {numeroReceta} no se corresponde entre Prensa {elemento[0]} y Transportador {elemento[1]}")
        return False
    
    # Check Transportador -> Apilador
    if elemento[1] != elemento[2]:
        print(f"La receta {numeroReceta} no se corresponde entre Transportador {elemento[1]} y Apilador {elemento[2]}")
        return False
    
    return True

def verificarRecetas(matriz):
    # Check if the entire matrix has all zero values
    if all(all(x == 0 for x in fila) for fila in matriz):
        print("Matriz de recetas NULA, SIN VALORES")
        return False
    
    # Enumerate through the matrix
    for i, fila in enumerate(matriz):
        if not comprobarPasoPieza(fila, i):
            return False
    
    return True

# Test cases
matriz1 = [
    [10, 10, 10],
    [8, 8, 8],
    [15, 15, 15],
    [5, 5, 5]
]

matriz2 = [
    [10, 10, 9],
    [8, 8, 8],
    [15, 14, 15],
    [5, 5, 5]
]

matriz3 = [
    [10, 10, 9],
    [8, 8, 8],
    [15, 15, 15],
    [5, 5, 6]
]

matriz4 = [
    [0, 0, 0],
    [8, 8, 8],
    [0, 0, 0],
    [5, 5, 5]
]

matriz5 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

assert verificarRecetas(matriz1) == True
assert verificarRecetas(matriz2) == False
assert verificarRecetas(matriz3) == False
assert verificarRecetas(matriz4) == True
assert verificarRecetas(matriz5) == False

print("All tests passed.")
