# calculo la duración en segundos
def duracion_a_segundos(cancion):
    duracion = cancion["duration"]

    tiempo = duracion.split(":") # divido para que quede mm:ss
    minutos = int(tiempo[0])
    segundos = int(tiempo[1])

    return minutos * 60 + segundos # todo a segundos asi calculo el tiempo total


# duracion total de la playlist
def duracion_total(playlist):
    total_segundos = 0

    for cancion in playlist:
        total_segundos += duracion_a_segundos(cancion)

    minutos_total = total_segundos // 60
    segundos_restantes = total_segundos % 60

    print(f"{minutos_total}m {segundos_restantes}s")

# cancion mas larga
def cancion_larga(playlist):
    return max(playlist,key=duracion_a_segundos)

# cancion mas corta
def cancion_corta(playlist):
    return min(playlist,key=duracion_a_segundos)