from collections import deque
from datetime import datetime

# Define the order class
class Pedido:
    def __init__(self, cliente, prioridad, tiempo_llegada):
        self.cliente = cliente
        self.prioridad = prioridad
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_espera = 0
    
    def __repr__(self):
        return f"Pedido({self.cliente}, {self.prioridad}, {self.tiempo_llegada}, {self.tiempo_espera})"

# Initialize the queues for each priority level
prioridad_alta = deque()
prioridad_media = deque()
prioridad_baja = deque()

# List to store processed orders
pedidos_procesados = []

# Function to register a new order
def nuevo_pedido(cliente, prioridad):
    tiempo_llegada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pedido = Pedido(cliente, prioridad, tiempo_llegada)
    if prioridad == 1:
        prioridad_alta.append(pedido)
    elif prioridad == 2:
        prioridad_media.append(pedido)
    elif prioridad == 3:
        prioridad_baja.append(pedido)
    return pedido

# Function to process the next order
def procesar_pedido():
    if prioridad_alta:
        pedido = prioridad_alta.popleft()
    elif prioridad_media:
        pedido = prioridad_media.popleft()
    elif prioridad_baja:
        pedido = prioridad_baja.popleft()
    else:
        return None
    # Update waiting time
    pedido.tiempo_espera = (datetime.now() - datetime.strptime(pedido.tiempo_llegada, "%Y-%m-%d %H:%M:%S")).total_seconds()
    pedidos_procesados.append(pedido)
    return pedido

# Function to show the number of pending orders
def pedidos_pendientes():
    return len(prioridad_alta) + len(prioridad_media) + len(prioridad_baja)

# Function to show the next order to be processed
def mostrar_proximo_pedido():
    if prioridad_alta:
        return prioridad_alta[0]
    elif prioridad_media:
        return prioridad_media[0]
    elif prioridad_baja:
        return prioridad_baja[0]
    return None

# Function to return statistics about the orders
def estadisticas():
    if not pedidos_procesados:
        return None, None
    max_espera = max(pedidos_procesados, key=lambda x: x.tiempo_espera)
    min_espera = min(pedidos_procesados, key=lambda x: x.tiempo_espera)
    return max_espera, min_espera

# ---------------------------Tests-----------------------------------

pedido1 = nuevo_pedido("Cliente1", 3)
pedido2 = nuevo_pedido("Cliente2", 1)
pedido3 = nuevo_pedido("Cliente3", 2)

# Verify the next order to be processed
assert mostrar_proximo_pedido() == pedido2, f"Expected {pedido2} but got {mostrar_proximo_pedido()}"

# Process orders and verify
assert procesar_pedido() == pedido2, f"Expected {pedido2} but got {procesar_pedido()}"
assert procesar_pedido() == pedido3, f"Expected {pedido3} but got {procesar_pedido()}"
assert procesar_pedido() == pedido1, f"Expected {pedido1} but got {procesar_pedido()}"

# Verify the number of pending orders
assert pedidos_pendientes() == 0, f"Expected 0 but got {pedidos_pendientes()}"

# Verify the processed orders
max_espera, min_espera = estadisticas()
assert max_espera == pedido1, f"Expected {pedido1} but got {max_espera}"
assert min_espera == pedido2, f"Expected {pedido2} but got {min_espera}"

print("All tests passed.")
