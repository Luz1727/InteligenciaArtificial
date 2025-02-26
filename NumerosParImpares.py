def es_par(num):
    """Verifica si un numero es par."""
    return num % 2 == 0

def suma_de_pares(a, b):
    """Verifica si la suma de dos numeros pares es par."""
    if es_par(a) and es_par(b):
        suma = a + b
        return True, suma
    return False, None

def main():
    # Interacción con el usuario
    print("Bienvenido a la demostración del teorema: La suma de dos números pares es siempre par.")
    
    numero1 = int(input("Introduce el primer número par: "))
    numero2 = int(input("Introduce el segundo número par: "))

    if es_par(numero1) and es_par(numero2):
        es_suma_par, resultado = suma_de_pares(numero1, numero2)
        if es_suma_par:
            print(f"La suma de {numero1} y {numero2} es {resultado}, que es un número par.")
        else:
            print("Error: la suma de los números ingresados no es par.")
    else:
        print("Al menos uno de los números no es par. Asegúrate de ingresar números pares.")

if __name__ == "__main__":
    main()
