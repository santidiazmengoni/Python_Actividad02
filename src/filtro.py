# filtro de spoilers
def filtro_spoilers(review):
    spoilers = input("Ingrese una lista de palabras consideradas spoilers separadas por coma: ")
    spoilers = spoilers.split(",")
    lista_spoilers = [spoiler.strip().lower() for spoiler in spoilers]

    palabras = review.split()

    for palabra in palabras:
        palabra_minuscula = palabra.lower().strip(".,")
        if palabra_minuscula in lista_spoilers:
            review = review.replace(palabra, len(palabra) * '*')
    print(review)