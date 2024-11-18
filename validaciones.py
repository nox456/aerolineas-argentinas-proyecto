######## Utilitarias ###########

def validarOpcion(n):
    valor = 0 # int
    while True:
        try:
            valor = int(n)
            if 1 <= valor <= 5:
                return valor
            else:
                print("ERROR: Opción no válida!")
                n = input("Ingrese una opción del menú (1-5): ")
        except ValueError:
            print("ERROR: Valor incorrecto!")
            n = input("Ingrese una opción del menú (1-5): ")


diccValidaciones = {
    "validarOpcion": validarOpcion
}
