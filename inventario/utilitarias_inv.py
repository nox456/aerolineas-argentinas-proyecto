# Utilitarias


def diccionario():
    return {
        "validarOpcion": validarOpcion,
        "leerArchivo": leerArchivo,
        "agregarArchivo": agregarArchivo,
        "validarInt": validarInt,
        "validarFloat": validarFloat,
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
        archivo = open("inventario/" + nombre)
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


def agregarArchivo(nombre):  # void
    archivo = object
    try:
        archivo = open("inventario/" + nombre, "a")
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
                print("ERROR: Solo se admiten valores mayores que cero")
                n = input("Ingrese el valor correcto: ")
        except ValueError:
            print("ERROR: Ingresó un valor no numérico")
            n = input("Ingrese el valor correcto: ")


def validarFloat(n):
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


validar = diccionario()
