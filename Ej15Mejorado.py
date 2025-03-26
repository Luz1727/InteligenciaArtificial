def main():
    nombre = (input("Ingresa tu nombre: "))
    producto = (input("Ingresa el nombre del producto: "))
    total_compra = float(input("Ingresa el total de tu compra: "))
    if total_compra > 100:
      descuento = total_compra * 0.10
      total_final = total_compra - descuento
      print(f"Felicidades {nombre} tienes un descuento del 10% de tu {producto}.\nEl total a pagar es: {total_final}")

if __name__ == "__main__":
    main()
