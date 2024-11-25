# Utilitarias


def diccionario():
    return {"opcion": validarOpcion}


def validarOpcion(n):  # int
    valor = 0  # int
    while True:
        try:
            valor = int(n)
            return valor
        except ValueError:
            print("ERROR: Valor incorrecto!")
            n = input("Ingrese un valor entero: ")


validar = diccionario()
