def main():
    total_compra = float(input("Ingresa el total de tu compra: "))
    
    if total_compra > 100:
        descuento = total_compra * 0.10
        total_final = total_compra - descuento
        print(f"Felicidades, tienes un descuento del 10%. El total a pagar es: {total_final:.2f}")
    else:
        print(f"El total a pagar es: {total_compra:.2f}")

if __name__ == "__main__":
    main()
