import time

def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print("Tiempo de inicio:", start_time)
        print("Tiempo de finalización:", end_time)
        print("Tiempo total:", total_time)
        return result
    return wrapper

@get_time
def mi_funcion():
    time.sleep(2)
    print("¡Función ejecutada!")

mi_funcion()