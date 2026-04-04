# validacion de email
def validacion_email(email):
    
    # contiene exactamente un @
    if email.count("@") != 1:
        return False
    
    # no empieza ni termina con @ ni con .
    if email[0] == "@" or email[-1] == "@" or email[0] == "." or email[-1] == ".":
        return False
    
    # divido antes y despues del @
    email = email.split("@")
    usuario = email[0]
    dominio = email[1]

    # tiene al menos un caracter antes del @
    if len(usuario) == 0:
        return False
    
    # tiene al menos un punto despues del @
    if "." not in dominio:
        return False
    
    # la parte despues del ultimo punto tiene al menos dos caracteres
    dominio_partes = dominio.split(".")
    if len(dominio_partes[-1]) < 2:
        return False
    
    return True