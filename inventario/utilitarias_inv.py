# Utilitarias


def diccionario():
    return {"validarOpcion": validarOpcion, "leerArchivo": leerArchivo}


def validarOpcion(n):  # int
    valor = 0  # int
    while True:
        try:
            valor = int(n)
            return valor
        except ValueError:
            print("ERROR: Valor incorrecto!")
            n = input("Ingrese un valor correcto")


def leerArchivo(ruta):
    archivo = object
    try:
        archivo = open(ruta, "rb")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


validar = diccionario()
