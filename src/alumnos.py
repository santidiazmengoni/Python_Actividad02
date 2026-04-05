# normalizacion de registros de alumnos

# validacion de nombre, Eliminar registros con nombre nulo, vacío o solo espacios
def validacion_nombre(nombre):
    return nombre is not None and nombre.strip() != ""

# validacion nota, Eliminar registros con nota nula, vacía o no numérica (como "absent")
def validacion_nota(nota):
    return nota is not None and nota.isdigit()

# normalizacion de nombres y estados, Normalizar nombres a formato título y estados a formato título
def normalizar_nombre(nombre):
    return nombre.strip().title()

def normalizar_estado(estado):
    return estado.strip().title()

# limpiar datos y generar listado final
def limpieza_datos(students):
    alumnos = {}

    for alumno in students:
        nombre = alumno["name"]
        nota = alumno["grade"]
        estado = alumno["status"]

        if validacion_nombre(nombre) and validacion_nota(nota):
            # hago la normalizacion
            nombre = normalizar_nombre(nombre)
            estado = normalizar_estado(estado)
            nota = int(nota)

            # Eliminar duplicados por nombre, quedándose con la nota más alta de cada alumno
            if nombre in alumnos:
                if nota > alumnos[nombre]["grade"]:
                    alumnos[nombre] = {"grade": nota, "status": estado}
            else:
                alumnos[nombre] = {"grade": nota, "status": estado}
    
    return alumnos

# Ordenar alfabéticamente por nombre
def ordenar_alfabeticamente(alumnos):
    nombres = list(alumnos.keys())
    nombres.sort()
    return nombres