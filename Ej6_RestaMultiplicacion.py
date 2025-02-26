def main():
    # EJERCICIO 6: RESTA Y MULTIPLICACIÓN
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    # Operaciones
    resta = n1 - n2
    multiplicacion = n1 * n2

    # Mostrar resultados
    print(f"El resultado de la resta de {n1} - {n2} es: {resta}")
    print(f"\nEl resultado de la multiplicación de {n1} * {n2} es: {multiplicacion}")
    print(f"\nPrograma realizado por Luz Arleth")

# Asegurar que solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()
