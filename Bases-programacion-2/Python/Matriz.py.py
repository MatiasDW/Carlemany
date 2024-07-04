class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def __add__(self, other):
        # Comprueba si el otro objeto es una instancia de la clase Matriz
        if isinstance(other, Matriz):
            # Crea una matriz vacía para almacenar el resultado de la suma
            result = []
            # Recorre las filas de la matriz
            for i in range(len(self.matriz)):
                # Crea una lista para almacenar los elementos de la fila resultante
                row = []
                # Recorre los elementos de cada fila
                for j in range(len(self.matriz[i])):
                    # Realiza la suma de los elementos correspondientes
                    element = self.matriz[i][j] + other.matriz[i][j]
                    # Agrega el elemento a la fila resultante
                    row.append(element)
                # Agrega la fila resultante a la matriz resultante
                result.append(row)
            # Devuelve una nueva instancia de la clase Matriz con la matriz resultante
            return Matriz(result)
        else:
            # Si el otro objeto no es una instancia de la clase Matriz, lanza un ValueError
            raise ValueError("Ambos operandos deben ser objetos de la clase Matriz")

    def __sub__(self, other):
        # Comprueba si el otro objeto es una instancia de la clase Matriz
        if isinstance(other, Matriz):
            # Crea una matriz vacía para almacenar el resultado de la resta
            result = []
            # Recorre las filas de la matriz
            for i in range(len(self.matriz)):
                # Crea una lista para almacenar los elementos de la fila resultante
                row = []
                # Recorre los elementos de cada fila
                for j in range(len(self.matriz[i])):
                    # Realiza la resta de los elementos correspondientes
                    element = self.matriz[i][j] - other.matriz[i][j]
                    # Agrega el elemento a la fila resultante
                    row.append(element)
                # Agrega la fila resultante a la matriz resultante
                result.append(row)
            # Devuelve una nueva instancia de la clase Matriz con la matriz resultante
            return Matriz(result)
        else:
            # Si el otro objeto no es una instancia de la clase Matriz, lanza un ValueError
            raise ValueError("Ambos operandos deben ser objetos de la clase Matriz")

    def __mul__(self, other):
        # Comprueba si el otro objeto es una instancia de la clase Matriz
        if isinstance(other, Matriz):
            # Comprueba si las dimensiones de las matrices son compatibles para la multiplicación
            if len(self.matriz[0]) != len(other.matriz):
                raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")
            # Crea una matriz vacía para almacenar el resultado de la multiplicación
            result = []
            # Recorre las filas de la primera matriz
            for i in range(len(self.matriz)):
                # Crea una lista para almacenar los elementos de la fila resultante
                row = []
                # Recorre los elementos de cada columna de la segunda matriz
                for j in range(len(other.matriz[0])):
                    # Inicializa el elemento de la fila resultante en 0
                    element = 0
                    # Recorre los elementos correspondientes de la primera y segunda matriz
                    for k in range(len(other.matriz)):
                        # Realiza la multiplicación y suma los productos parciales
                        element += self.matriz[i][k] * other.matriz[k][j]
                    # Agrega el elemento a la fila resultante
                    row.append(element)
                # Agrega la fila resultante a la matriz resultante
                result.append(row)
            # Devuelve una nueva instancia de la clase Matriz con la matriz resultante
            return Matriz(result)
        else:
            # Si el otro objeto no es una instancia de la clase Matriz, lanza un ValueError
            raise ValueError("El segundo operando debe ser un objeto de la clase Matriz")

    def mostrar(self):
        # Imprime los elementos de la matriz
        for row in self.matriz:
            print(row)


# Ejemplo de uso
matriz1 = Matriz([[1, 2, 3],
                  [4, 5, 6]])
matriz2 = Matriz([[1, 1, 1],
                  [1, 1, 1]])
matriz_resultado = matriz1 + matriz2
matriz_resultado.mostrar()