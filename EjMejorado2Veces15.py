import datetime
import random
def main():
    numero_aleatorio = random.randint(1,100)
    tienda = input("Ingresa el nombre de la tienda: ")
    nombre = input("Ingresa el nombre del cliente: ")
    producto = input("Ingresa el nombre del producto: ")
    total_compra = float(input("Ingresa el total de tu compra: "))


    descuento = 0  
    total_final = total_compra  

    if total_compra > 100:
      descuento = total_compra * 0.10
      total_final = total_compra - descuento

      fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


      print("\n-------------------------------------- TICKET DE COMPRA --------------------------------------\n")
      print(f"                                          TIENDA {tienda}                                             ")
      print(f"Folio: {numero_aleatorio}")
      print(f"Fecha y hora de su compra: {fecha}")
      print(f"Cliente: {nombre}")
      print(f"\nNombre del producto: {producto}")
      print(f"Total de la compra: ${total_compra:.2f}")
      print(f"Descuento aplicado: ${descuento:.2f}")
      print(f"El total a pagar es: ${total_final:.2f}")
      print(f"\n---------------------------------- ¡GRACIAS POR SU COMPRA! -----------------------------------")



if __name__ == "__main__":
    main()
