# amigo invisible random
import random

# armo la lista de los participantes
def lista_participantes(nombres):
    # saco los espacios extras
    participantes = [nombre.strip() for nombre in nombres.split(",")]
    return participantes

# valido la lista si cumple con las condiciones
def validacion_participantes(participantes):
    # debe haber al menos 3 participantes
    if len(participantes) < 3:
        return False

    # no debe haber nombres duplicados
    participantes_normalizado = [par.lower() for par in participantes]
    if len(participantes_normalizado) != len(set(participantes_normalizado)):
        return False
    
    return True

# hago el sorteo
def sorteo_amigo(participantes):
    copia_participantes = participantes.copy()

    while True:
        random.shuffle(copia_participantes)

        esta_bien = True
        for i in range(len(participantes)):
            if participantes[i] == copia_participantes[i]:
                esta_bien = False
                break # si uno esta asignado a si mismo sale del for y continua de vuelta al while
        
        if esta_bien:
            break # si nadie esta asignado consigo mismo sale del while

    asignaciones = {}
    for i in range(len(participantes)):
        asignaciones[participantes[i]] = copia_participantes[i]
    
    return asignaciones