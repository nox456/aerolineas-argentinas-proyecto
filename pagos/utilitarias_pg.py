# Utilitarias


def diccionario():
    return {
        "validarOpcion": validarOpcion,
        "leerArchivo": leerArchivo,
        "validarFloat": validarFloat,
        "validarInt": validarInt,
        "escribirArchivo": escribirArchivo,
        "validarDia": validarDia,
        "validarMes": validarMes,
        "validarAno": validarAno,
        "validarNombre": validarNombre,
        "manejoNombre": manejoNombre
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
        archivo = open("pagos/" + nombre, "rb")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


def escribirArchivo(nombre):
    archivo = object
    try:
        archivo = open("pagos/" + nombre, "wb")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


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


def validarDia(dia):  # int
    while True:
        dia = validarInt(dia)
        if 1 <= dia <= 31:
            return dia
        dia = input("Ingrese un día válido: ")


def validarMes(mes):  # int
    while True:
        mes = validarInt(mes)
        if 1 <= mes <= 12:
            return mes
        mes = input("Ingrese un mes válido: ")


def validarAno(ano):  # int
    while True:
        ano = validarInt(ano)
        if ano >= 1950:
            return ano
        ano = input("Ingrese un año válido: ")


def validarNombre(nombre):
    tupla = (
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        " ",
        "@",
        "#",
        "$",
        "!",
        "%",
        "&",
        ".",
        ",",
        ":",
        ";",
        "*",
        "+",
        "-",
        "_",
        "¿",
        "?",
        "¡",
    )
    for i in range(len(nombre)):
        for j in range(len(tupla)):
            if nombre[i] == tupla[j]:
                return False
    return True


def manejoNombre(nombre):
    while True:
        if validarNombre(nombre) == False:
            nombre = input("Ingrese un nombre o apellido válido: ")
        else:
            return nombre


validar = diccionario()
