def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        # Cifrar mayúsculas
        if char.isupper():
            resultado += chr((ord(char) + desplazamiento - 65) % 26 + 65)
        # Cifrar minúsculas
        elif char.islower():
            resultado += chr((ord(char) + desplazamiento - 97) % 26 + 97)
        else:
            resultado += char # Mantener espacios/caracteres especiales
    return resultado

# Ejemplo de uso
texto = "Hola Mundo"
clave = 3
texto_cifrado = cifrado_cesar(texto, clave)
print("Texto Cifrado:", texto_cifrado) # Resultado: Krod Pxqgr
