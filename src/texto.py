# devuelve la cantidad de lineas del texto
def cantidad_lineas(text):
    return len(text.split("\n"))


# cantidad de palabras
def cantidad_palabras(text):
    total_palabras = 0
    lineas = text.split("\n")

    for linea in lineas:
        palabras = linea.split()
        total_palabras += len(palabras)

    return total_palabras

# promedio por lineas
def promedio_lineas(text):
    numero = cantidad_palabras(text) / cantidad_lineas(text)

    return round(numero,2)

# lineas por encima del promedio 
def lineas_por_encima(text):
    lineas = text.split("\n")
    promedio = promedio_lineas(text)

    resultado = []
    
    for linea in lineas:
        if len(linea.split()) > promedio:
            resultado.append(linea)

    return resultado 

