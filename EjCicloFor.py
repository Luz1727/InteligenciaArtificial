def main():
    cantidad = int(input("Ingrese la cantidad de calificaciones: "))
    suma = 0

    for i in range(cantidad):
        calif = int(input("Ingrese la calificación: "))
        suma += calif

    promedio = suma / cantidad
    print("El promedio es:", promedio)
    
if __name__ == "__main__":
    main()
