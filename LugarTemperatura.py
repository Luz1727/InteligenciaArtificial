def determinar_estado_por_temperatura(temperatura):
    if 48 <= temperatura <= 50:
        return "Sonora"
    elif 45 <= temperatura <= 47:
        return "Sonora"
    elif 42 <= temperatura <= 44:
        return "Oaxaca y Pinotepa"
    elif 39 <= temperatura <= 41:
        return "Oaxaca"
    elif 36 <= temperatura <= 38:
        return "Putla"
    elif 33 <= temperatura <= 35:
        return "Tlaxiaco"
    elif 30 <= temperatura <= 32:
        return "Oaxaca"
    elif 27 <= temperatura <= 29:
        return "Chiapas"
    elif 24 <= temperatura <= 26:
        return "Puebla"
    elif 21 <= temperatura <= 23:
        return "Veracruz"
    elif 18 <= temperatura <= 20:
        return "Tehuacán, Puebla"
    elif 15 <= temperatura <= 17:
        return "Chiapas"
    elif 12 <= temperatura <= 14:
        return "Yucatán"
    elif 9 <= temperatura <= 11:
        return "Mérida"
    elif 0 <= temperatura <= 8:
        return "EUA"
    else:
        return "NA"

def main():
    temperatura = int(input("Ingresa la temperatura que desea saber: "))
    estado = determinar_estado_por_temperatura(temperatura)
    if estado != "NA":
        print(f"\nEl lugar que se encuentra entre el rango de temperatura {temperatura}°C es: {estado}")
    else:
        print("\nTemperatura fuera del rango definido.")

if __name__ == "__main__":
    main()
