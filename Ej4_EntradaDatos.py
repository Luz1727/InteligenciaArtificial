def main():
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    altura = float(input("¿Cuánto mides? (en metros) "))

    # Mostrar los datos introducidos
    print("Hola", nombre, "Tienes", edad, "años y mides", altura, "metros")

# Asegurar que solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()
