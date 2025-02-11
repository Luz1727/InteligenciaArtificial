#Ejercicio 7 Calcular el area de un circulo
import math

radio=float(input("Ingrese la radio del circulo: \n "))
area= math.pi * (radio**2)

print(f"El area del circulo con radio {radio} es: {area:.2f} metros cuadrados")