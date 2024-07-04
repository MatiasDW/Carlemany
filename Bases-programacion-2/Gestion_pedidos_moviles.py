from queue import Queue
from datetime import datetime

# Initialize the queues and delivered orders list
priority_queue = Queue()
normal_queue = Queue()
delivered_orders = []

# Define the order class
class Order:
    def __init__(self, nombre_cliente, apellido_cliente, cantidad_moviles, prioridad):
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.cantidad_moviles = cantidad_moviles
        self.prioridad = prioridad
        self.fecha_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __repr__(self):
        return f"Order({self.nombre_cliente}, {self.apellido_cliente}, {self.cantidad_moviles}, {self.prioridad}, {self.fecha_pedido})"

# Function to add an order
def hacer_pedido(nombre_cliente, apellido_cliente, cantidad_moviles, prioridad):
    pedido = Order(nombre_cliente, apellido_cliente, cantidad_moviles, prioridad)
    if prioridad == 1:
        priority_queue.put(pedido)
    else:
        normal_queue.put(pedido)
    return pedido

# Function to view pending orders
def ver_pedidos_pendientes():
    pendientes = list(priority_queue.queue) + list(normal_queue.queue)
    return pendientes

# Function to deliver an order
def entregar_pedido():
    if not priority_queue.empty():
        pedido = priority_queue.get()
    elif not normal_queue.empty():
        pedido = normal_queue.get()
    else:
        return None
    delivered_orders.append(pedido)
    return pedido

# Function to view delivered orders
def ver_pedidos_entregados():
    return delivered_orders

# Function to check waiting time for an order
def consultar_tiempo_para_pedido(nombre_cliente, apellido_cliente):
    # Count the orders before the specified order
    count = 0
    for pedido in list(priority_queue.queue):
        if pedido.nombre_cliente == nombre_cliente and pedido.apellido_cliente == apellido_cliente:
            return count
        count += 1
    for pedido in list(normal_queue.queue):
        if pedido.nombre_cliente == nombre_cliente and pedido.apellido_cliente == apellido_cliente:
            return count
        count += 1
    return -1  # If the order is not found

# ---------------------------Tests-----------------------------------

pedido1 = hacer_pedido("Pepito", "Perez", 5, 2)
pedido2 = hacer_pedido("Maria", "Fernandez", 3, 1)
pedido3 = hacer_pedido("Joan", "Jimenez", 2, 2)

# Verify added orders
pendientes = ver_pedidos_pendientes()
assert pendientes == [pedido2, pedido1, pedido3], f"Expected [pedido2, pedido1, pedido3] but got {pendientes}"

# Deliver an order
pedido_entregado = entregar_pedido()
assert pedido_entregado == pedido2, f"Expected {pedido2} but got {pedido_entregado}"

# Verify delivered orders
entregados = ver_pedidos_entregados()
assert entregados == [pedido_entregado], f"Expected [{pedido_entregado}] but got {entregados}"

# Check waiting time for an order
tiempo_espera = consultar_tiempo_para_pedido("Pepito", "Perez")
assert tiempo_espera == 0, f"Expected 0 but got {tiempo_espera}"

# Deliver the other orders to complete the test
entregar_pedido()
entregar_pedido()

# Verify all orders have been delivered
entregados = ver_pedidos_entregados()
assert len(entregados) == 3, f"Expected 3 but got {len(entregados)}"

print("All tests passed.")
