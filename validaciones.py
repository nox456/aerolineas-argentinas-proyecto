# Utilitarias


def validarOpcion():  # int
    valor = 0  # int
    while True:
        try:
            valor = int(input("Ingrese una opción del menú (1-5): "))
            return valor
        except ValueError:
            print("ERROR: Valor incorrecto!")


validar = {"opcion": validarOpcion}
