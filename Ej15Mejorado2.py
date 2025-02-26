import datetime
def main():
    tienda = input("Ingresa el nombre de la tienda: ")
    nombre = input("Ingresa el nombre del cliente: ")
    producto = input("Ingresa el nombre del producto: ")
    total_compra = float(input("Ingresa el total de tu compra: "))

# Inicializar descuento y total_final
    descuento = 0  
    total_final = total_compra  

    if total_compra > 100:
      descuento = total_compra * 0.10
      total_final = total_compra - descuento

      fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Impresión del ticket
      print("\n-------------------------------------- TICKET DE COMPRA --------------------------------------\n")
      print(f"                                          Tienda {tienda}                                             ")
      print(f"\nFecha y hora de su compra: {fecha}")
      print(f"\nNombre del cliente: {nombre}")
      print(f"\nNombre del producto: {producto}")
      print(f"\nTotal de la compra: ${total_compra:.2f}")
      print(f"\nDescuento aplicado: ${descuento:.2f}")
      print(f"\nEl total a pagar es: ${total_final:.2f}")

if __name__ == "__main__":
    main()
