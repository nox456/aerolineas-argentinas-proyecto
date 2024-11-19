# Utilitarias


def validarOpcion():  # int
    valor = 0  # int
    while True:
        try:
            valor = int(input("Ingrese una opción del menú (1-5): "))
            return valor
        except ValueError:
            print("ERROR: Valor incorrecto!")


def openFile(ruta):  # object archivo
    try:
        archivo = open(ruta, "rb")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


validar = {"opcion": validarOpcion, "abrirArchivo": openFile}
