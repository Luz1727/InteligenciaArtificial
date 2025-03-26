def main():
    num = float(input("Ingrese un número: "))  
    if num > 0:
      print(f"El número {num} es mayor a cero.")
    elif num < 0:
     print(f"El número {num} es menor a cero.")
    else:
      print(f"El número es cero.")  
if __name__ == "__main__":
    main()