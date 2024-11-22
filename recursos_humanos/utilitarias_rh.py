# Utilitarias


def diccionario():
    return {
        "opcion": validarOpcion,
        "leerArchivo": leerArchivo,
        "agregarArchivo": agregarArchivo,
        "entero": validarInt,
    }


def validarOpcion(n):  # int
    valor = 0  # int
    while True:
        try:
            valor = int(n)
            return valor
        except ValueError:
            print("ERROR: Valor incorrecto!")
            n = input("Ingrese un valor correcto")


def leerArchivo(nombre):  # object archivo
    archivo = object

    try:
        archivo = open("recursos_humanos/" + nombre, "rb")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


def agregarArchivo(nombre):  # object archivo
    archivo = object
    try:
        archivo = open("recursos_humanos/" + nombre, "ab")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


def validarInt(n):
    valor = 0  # int
    while True:
        try:
            valor = int(n)
            if valor > 0:
                return valor
            else:
                print("ERROR: No se admiten valores negativos!")
                n = input("Ingrese el valor correcto: ")
        except ValueError:
            print("ERROR: Valor incorrecto!")
            n = input("Ingrese el valor correcto: ")


validar = diccionario()
