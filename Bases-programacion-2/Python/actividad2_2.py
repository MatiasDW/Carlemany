def modificar_valor(valor):
    valor += 1
    print("Dentro de la función:", valor)

def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función:", lista)

# Paso de parámetros por valor (objeto inmutable)
x = 10
print("Antes de llamar a modificar_valor:", x)
modificar_valor(x)
print("Después de llamar a modificar_valor:", x)

# Paso de parámetros por referencia (objeto mutable)
my_list = [1, 2, 3]
print("Antes de llamar a modificar_lista:", my_list)
modificar_lista(my_list)
print("Después de llamar a modificar_lista:", my_list)