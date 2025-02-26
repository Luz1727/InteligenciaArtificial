class Agente:
    def __init__(self, nombre, ubicacion):  # Corregido el nombre del constructor
        self.nombre = nombre  # Corregida la asignación de nombre
        self.ubicacion = ubicacion

    def mover(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"{self.nombre} se movió a {self.ubicacion}")

# Creación de objetos
agente1 = Agente("Agente 1", "A")
agente2 = Agente("Agente 2", "B")

# Movimiento de los agentes
agente1.mover("C")
agente2.mover("C")

# Verificación de encuentro
if agente1.ubicacion == agente2.ubicacion:
    print("Los agentes se han encontrado en el punto C")
else:
    print("Los agentes no se han encontrado")
