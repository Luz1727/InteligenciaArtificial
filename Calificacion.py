def main():
    cal = float(input("Ingrese una calificación: "))  

    if cal <= 100 and cal >=95 :
        print(f"La calificación es excelente")
    elif cal <=94 and cal >=85:
        print(f"La calificacion es notable")
    elif cal <=84 and cal >= 75:
     print(f"La calificacion es regular")
    elif cal <=74 and cal >= 70:
     print(f"La calificacion es sufuciente")
    else:
     print(f"NA")

if __name__ == "__main__":
    main()