opciones = ["ir al cine", "estudiar", "Hacer ejercicio"]

def tomar_decision(prioridades):
    for opcion in opciones:
        if opcion in prioridades:
            return f"El agente no decide nada."
prioridades = ["hacer ejercicio", "estudiar"]
print(tomar_decision(prioridades))