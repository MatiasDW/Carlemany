import heapq

def lista_bajo_dos_ordenes(m, autor):
    # Filtrar la matriz para obtener solo los libros del autor especificado
    libros_autor = [fila for fila in m if fila[0] == autor]
    
    # Si el autor no tiene libros, devolver una lista vacía
    if not libros_autor:
        return []
    
    # Ordenar los libros por ventas de menor a mayor
    libros_ordenados = heapq.nsmallest(2, libros_autor, key=lambda x: x[3])
    
    # Devolver una lista con los títulos de los dos libros con menos ventas
    return [libro[1] for libro in libros_ordenados]

# Matriz de ejemplo
matriz = [
    ["Platón", "La República", -380, 500000],
    ["Platón", "Menón", -385, 460000],
    ["Platón", "El Banquete", -385, 450000],
    ["Aristóteles", "Ética a Nicómaco", -340, 600000],
    ["Aristóteles", "Metafísica", -350, 550000],
    ["Aristóteles", "Poética", -335, 530000],
    ["Nietzsche", "La genealogía de la moral", 1887, 650000],
    ["Friedrich Nietzsche", "Así habló Zaratustra", 1883, 700000],
    ["Kant", "Crítica de la razón pura", 1781, 900000],
    ["Kant", "Fundamentación de la metafísica de las costumbres", 1785, 750000],
    ["Nietzsche", "Así habló Zaratustra", 1883, 700000],
    ["Descartes", "Las pasiones del alma", 1649, 800000],
    ["Hegel", "Fenomenología del espíritu", 1807, 920000],
    ["Hegel", "Enciclopedia de las ciencias filosóficas", 1817, 880000],
    ["Hegel", "Principios de la filosofía del derecho", 1820, 860000],
    ["Hegel", "Lecciones sobre la filosofía de la historia", 1837, 840000],
    ["Nietzsche", "El anticristo", 1895, 770000],
    ["Nietzsche", "Más allá del bien y del mal", 1886, 800000],
    ["Nietzsche", "Ecce Homo", 1888, 790000],
]

# Comprobación de que la función maneje al menos tres libros de un mismo autor
assert lista_bajo_dos_ordenes(matriz, 'Platón') == ['El Banquete', 'Menón']

# Que la función nos entregue lo correcto con un número múltiple de libros y ordenados de forma intercalada en la matriz
assert lista_bajo_dos_ordenes(matriz, 'Nietzsche') == ['La genealogía de la moral', 'Así habló Zaratustra']

# Que la función maneje autores que no salen en la lista y no nos dé error
assert lista_bajo_dos_ordenes(matriz, 'Guille Deleuze') == []

# Que la función maneje casos donde solo haya dos obras en un autor
assert lista_bajo_dos_ordenes(matriz, 'Kant') == ["Fundamentación de la metafísica de las costumbres", "Crítica de la razón pura"]

# Que la función maneje casos donde solo haya una obra por autor
assert lista_bajo_dos_ordenes(matriz, 'Descartes') == ["Las pasiones del alma"]

print("All tests passed.")
