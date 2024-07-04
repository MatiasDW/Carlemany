from queue import priorityQueue
import filecmp

#Function to add packages to the server
def add_package(server, expiration, priority):
    server.put((priority, expiration))
    print(f"Packete con expiracion agregada {expiration} y prioridad {priority}")

#Function to process packages in the server
def process(server, current_time):
    lost_packages = 0
    print(f"Procesando a la hora {current_time}")
    while not server.empty():
        priority, expiration = server.get()
        print(f"Revisando paquete con expiracion {expiration} y prioridad {priority}")
        if expiration > current_time:
            server.put((priority, expiration))
            print("paquete aun es valido ponerlo de vuelta en Queue")
            break
        else:
            lost_packages += 1 
            print("Paquete expirado, contar como perdido")
        return lost_packages

#Main function for priority server simulator
def priority_server_simulator(path_in, path_out):
    server = PriorityQueue()
    lost_packages = 0
    current_time = 0

    with open(path_in) as f, open(path_out, "w") as f_out:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("t "):
                current_time = int(line.split()[1])
                lost_packages += process(server, current_time)
            elif linestarswith("package "):
                _, expiration, priority = line.split()
                add_package(server, int(expiration), int(priority))
            elif line == "lost":
                f_out.write(f"{lost_packages}\n")
            
#Test the main function with a sample file
priority_server_simulator("test_server_prioridad.txt", "test_server_prioridad_output.txt")

#Validate the result by comparing files
assert filecmp.cmp("test_server_prioridad_output.txt", "test_server_prioridad_salida_correcta.txt")