def main():
    # Pedir el primer número
    numero1 = float(input("Introduce el primer número: \n"))

    # Pedir el segundo número
    numero2 = float(input("Introduce el segundo número: \n"))

    # Realizar una operación
    suma = numero1 + numero2

    # Mostrar el resultado con salto de línea
    print(f"\nLa suma de {numero1} y {numero2} es: {suma}")

# Asegurar que solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()
