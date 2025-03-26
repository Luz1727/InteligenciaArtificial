class Nodo:
    def __init__(self, calificacion):
        self.calificacion = calificacion
        self.siguiente = None

class ListaCalificaciones:
    def __init__(self):
        self.cabeza = None

    def agregar_calificacion(self, calificacion):
        nuevo_nodo = Nodo(calificacion)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def calcular_promedio(self):
        if self.cabeza is None:
            return 0

        total = 0
        contador = 0
        actual = self.cabeza

        while actual is not None:
            total += actual.calificacion
            contador += 1
            actual = actual.siguiente

        return total / contador

def main():
    lista = ListaCalificaciones()

    n = int(input("¿Cuántas calificaciones deseas ingresar? "))

    for _ in range(n):
        calificacion = float(input("Ingresa una calificación: "))
        lista.agregar_calificacion(calificacion)

    promedio = lista.calcular_promedio()
    print(f"El promedio de las {n} calificaciones es: {promedio:.2f}")

if __name__ == "__main__":
    main()
