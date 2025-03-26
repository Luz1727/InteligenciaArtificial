def main():
    nombre=input(("Ingrese su nombre completo: "))
    materia=input(("Ingrese el nombre de la materia: "))

    cal = float(input("Ingrese una calificación: \n"))  
    if cal <= 100 and cal >=95 :
      print(f"La calificación {cal} es excelente")
    elif cal <=94 and cal >=85:
     print(f"La calificacion {cal} es notable")
    elif cal <=84 and cal >= 75:
     print(f"La calificacion {cal} es regular")
    elif cal <=74 and cal >= 70:
     print(f"La calificacion {cal} es sufuciente")
    else:
     print(f"NA")
     print(f"nombre: ", nombre,  f"\nnombre de la materia", materia)
if __name__ == "__main__":
    main()