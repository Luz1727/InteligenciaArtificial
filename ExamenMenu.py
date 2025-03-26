import Programa1
import Programa2
import Ej1DeclaracionVariable
import Ej2_DeclaracionVariable_Suma
import Ej4_EntradaDatos
import Ej5_EntradaDatosSuma
import Ej6_RestaMultiplicacion
import Ej7_AreaCirculo
import Ej8_NumeroParImpar
import ejercicioAND
import Calificacion
import EjercicioNombreMateria
import ejIf
import Ej10_Mayor
import Ej11_NumeroPositivo
import Ej12_AdivinarNumero
import Ej14_MostrarCalifLetra
import Ej15_CompraDescuento
import Ej15Mejorado
import EjMejorado2Veces15
import ElegirTemperatura
import LugarTemperatura


def mostrar_menu():
    print("\n--- MENÚ DE EJERCICIOS ---")
    print("1. Ejercicio 1 - La suma de 2 numeros")
    print("2. Ejercicio 2 - Ingresar los datos de un alumno desde teclado")
    print("3. Ejercicio 3 - Declaración de Variables")
    print("4. Ejercicio 4 - Suma de Variables")
    print("5. Ejercicio 5 - Entrada de Datos")
    print("6. Ejercicio 6 - Entrada de Datos con Suma")
    print("7. Ejercicio 7 - Resta y Multiplicación")
    print("8. Ejercicio 8 - Área del Círculo")
    print("9. Ejercicio 9 - Saber si un numero es par o impar")
    print("10. Ejercicio 10 - Saber si un numero ingresado se encuentra entre ese rango")
    print("11. Ejercicio 11 - Ingresar una calificación y saber si se encuentra entre el rango de NA 0 excelente")
    print("12. Ejercicio 12 - Ingresar el nombre, materia y calificacion y mostrar si la calificación es buena")
    print("13. Ejercicio 13 - Ingresar un numero y mostrar si es menor, mayor o igual a cero")
    print("14. Ejercicio 14 - Ingresar un numero e imprimir si es o no mayor a 10")
    print("15. Ejercicio 15 - Ingresar un numero e imprimir si es positivo, negativo o cero")
    print("16. Ejercicio 16 - Adivinar un numero utilizando numeros aleatorios")
    print("17. Ejercicio 17 - Ingresar calificacion y mostrar (A, B, C, D o F)")
    print("18. Ejercicio 18 - Ingresar el total de compra y mostrar el total con descuento")
    print("19. Ejercicio 19 - datos desde el teclado y mostrar el total de la compra con el descuento")
    print("20. Ejercicio 20 - Ingresar datos desde teclado y mostrar el tiket de una tienda")
    print("21. Ejercicio 21 - Elegir una de las opciones para saber la temperatura (madrugada, amanecer, mañana, mediodia, tarde, noche)")
    print("22. Ejercicio 22 - Ingresar los grados de temperatura y el programa muestra el lugar que se encuentra a esos grados")   
    print("0. Salir")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        Programa1.main()
    elif opcion == "2":
        Programa2.main()
    elif opcion == "3":
        Ej1DeclaracionVariable.main()
    elif opcion == "4":
        Ej2_DeclaracionVariable_Suma.main()
    elif opcion == "5":
        Ej4_EntradaDatos.main()
    elif opcion == "6":
        Ej5_EntradaDatosSuma.main()
    elif opcion == "7":
        Ej6_RestaMultiplicacion.main()
    elif opcion == "8":
        Ej7_AreaCirculo.main()
    elif opcion == "9":
        Ej8_NumeroParImpar.main()
    elif opcion == "10":
        ejercicioAND.main()
    elif opcion == "11":
        Calificacion.main()
    elif opcion == "12":
        EjercicioNombreMateria.main()
    elif opcion == "13":
        ejIf.main()
    elif opcion == "14":
        Ej10_Mayor.main()
    elif opcion == "15":
        Ej11_NumeroPositivo.main()
    elif opcion == "16":
        Ej12_AdivinarNumero.main()
    elif opcion == "17":
        Ej14_MostrarCalifLetra.main()
    elif opcion == "18":
        Ej15_CompraDescuento.main()
    elif opcion == "19":
        Ej15Mejorado.main()
    elif opcion == "20":
        EjMejorado2Veces15.main()
    elif opcion == "21":
        ElegirTemperatura.main()
    elif opcion == "22":
        LugarTemperatura.main()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
        
