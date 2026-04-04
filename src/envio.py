# calcular costo de envio
def costo_envio(peso,zona):
    zona = zona.lower() 

    # caso donde no se ingrese zona correctamente
    if zona not in ["local","regional","nacional"]:
        return -1
    
    # peso <= 1
    if peso <= 1:
        if zona == "local":
            return 500
        elif zona == "regional":
            return 1000
        else:
            return 2000
    
    # peso <= 5
    elif peso <= 5:
        if zona == "local":
            return 1000
        elif zona == "regional":
            return 2500
        else:
            return 4500
        
    # peso < 5
    else:
        if zona == "local":
            return 2000
        elif zona == "regional":
            return 5000
        else:
            return 8000
    