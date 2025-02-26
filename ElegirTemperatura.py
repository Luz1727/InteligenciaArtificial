def main():
    datos_temperatura = {
        "madrugada" : 20,
        "amanecer" : 15,
        "mañana" : 20,
        "mediodia" : 30 ,
        "tarde" : 25,
        "noche" : 20
}

    def predecir_temperatura(hora):
        if hora == "madrugada":
            return datos_temperatura["madrugada"]
        elif hora == "amanecer":
            return datos_temperatura["amanecer"]
        elif hora == "mañana":
            return datos_temperatura["mañana"]
        elif hora == "mediodia":
            return datos_temperatura["mediodia"]
        elif hora == "tarde":
            return datos_temperatura["tarde"]
        if hora == "noche":
            return datos_temperatura["noche"]
        else:
            return "Hora no valida"

    hora = (input("Elige la opcion de la temperatura que quisieras saber:  \nmadrugada, amanecer, mañana, mediodia, tarde, noche \n"))
    print(f"La temperatura promedio en la {hora} es: {predecir_temperatura(hora)} grados")

if __name__ == "__main__":
    main()
