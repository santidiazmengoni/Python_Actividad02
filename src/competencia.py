# simulación de competencia de cocina y ranking

# calculo el puntaje de la ronda
def calcular_ronda(scores):
    puntajes = {}

    for participante in scores:
        jueces = scores[participante]
        puntaje_total = jueces["judge_1"] + jueces["judge_2"] + jueces["judge_3"]
        puntajes[participante] = puntaje_total

    return puntajes

# inicializo los datos que luego voy a ir actualizando 
def inicializar_datos(participantes):
    datos = {}

    for participante in participantes:
        datos[participante] = {
            "total_puntos": 0,
            "rondas_jugadas": 0,
            "mejor_ronda": 0,
            "rondas_ganadas": 0
        }
    
    return datos

# actualizo los datos a medida que avanzan las rondas
def actualizar_datos(datos, puntaje_ronda):
    
    ganador = max(puntaje_ronda, key=puntaje_ronda.get) 
    max_puntaje = puntaje_ronda[ganador]

    for participante in puntaje_ronda:
        puntaje = puntaje_ronda[participante]

        datos[participante]["total_puntos"] += puntaje
        datos[participante]["rondas_jugadas"] += 1

        if puntaje > datos[participante]["mejor_ronda"]:
            datos[participante]["mejor_ronda"] = puntaje
    
    datos[ganador]["rondas_ganadas"] += 1

    return {
        "ganador": ganador,
        "puntaje": max_puntaje
    }

# imprimo la tabla con los datos de los participantes
def imprimir_tabla(datos):
    def obtener_total(nombre):
        return datos[nombre]["total_puntos"]

    ordenados = list(datos.keys())
    ordenados.sort(key=obtener_total, reverse=True)

    print("Cocinero      Puntaje    Rondas ganadas    Mejor ronda    Promedio")
    print("-------------------------------------------------------------------")

    for participante in ordenados:
        total = datos[participante]["total_puntos"]
        ganadas = datos[participante]["rondas_ganadas"]
        mejor = datos[participante]["mejor_ronda"]
        rondas = datos[participante]["rondas_jugadas"]
        promedio = total / rondas

        print(f"{participante:<13} {total:<10} {ganadas:<17} {mejor:<14} {promedio:.1f}")
    
    print("-------------------------------------------------------------------")
