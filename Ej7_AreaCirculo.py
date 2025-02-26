import math

def main():
    # Ejercicio 7: Calcular el área de un círculo
    radio = float(input("Ingrese el radio del círculo: \n "))
    area = math.pi * (radio**2)

    # Mostrar el resultado
    print(f"El área del círculo con radio {radio} es: {area:.2f} metros cuadrados")

# Asegurar que solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()