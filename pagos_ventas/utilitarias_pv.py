# Utilitarias


def diccionario():
    return {"validarOpcion": validarOpcion, "leerArchivo": leerArchivo}


def validarOpcion(n):
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
        archivo = open("pagos_ventas/" + nombre)
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


validar = diccionario()
