#Diccionario que almacenara las temperaturas por ciudad y hora
datos_temperatura ={
    "Madrid": {"mañana": 20, "tarde": 25, "noche": 18},
    "Barcelona": {"mañana0": 22, "tarde": 27, "noche": 20}
}

def predecir_temperatura(ciudad, hora):
    if ciudad in datos_temperatura:
        if hora in datos_temperatura[ciudad]:
            return datos_temperatura[ciudad][hora]
        else:
            return"Hora no valida en esta ciudad"
    else: 
        return "Ciudad no válida"
    
def agregar_datos_temperatura (ciudad, hora, temperatura):
    if ciudad not in datos_temperatura:
        datos_temperatura[ciudad] = {}
    datos_temperatura[ciudad][hora] = temperatura
    print(f"Datos agregados: {ciudad} - {hora} - {temperatura} grados")
    