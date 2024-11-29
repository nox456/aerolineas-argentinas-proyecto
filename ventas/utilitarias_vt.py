# Utilitarias


def diccionario():
    return {
        "validarOpcion": validarOpcion,
        "leerArchivo": leerArchivo,
        "validarInt": validarInt,
        "validarFloat": validarFloat,
        "escribirArchivo": escribirArchivo
    }


def validarOpcion(n):  # int
    valor = 0  # int
    while True:
        try:
            valor = int(n)
            return valor
        except ValueError:
            print("ERROR: Valor incorrecto!")
            n = input("Ingrese un valor correcto: ")


def leerArchivo(nombre):
    archivo = object
    try:
        archivo = open("ventas/" + nombre, "rb")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


def validarInt(n):  # int
    valor = 0  # int
    while True:
        try:
            valor = int(n)
            if valor > 0:
                return valor
            else:
                print("ERROR: Solo se admiten valores mayores que cero")
                n = input("Ingrese el valor correcto: ")
        except ValueError:
            print("ERROR: Ingresó un valor no numérico")
            n = input("Ingrese el valor correcto: ")


def validarFloat(n):  # float
    valor = 0.0  # float
    while True:
        try:
            valor = float(n)
            if valor > 0:
                return valor
            else:
                print("ERROR: Solo se admiten valores mayores que cero")
                n = input("Ingrese el valor correcto: ")
        except ValueError:
            print("ERROR: Ingresó un valor no numérico")
            n = input("Ingrese el valor correcto: ")


def escribirArchivo(nombre):
    archivo = object
    try:
        archivo = open("ventas/" + nombre, "wb")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


validar = diccionario()
