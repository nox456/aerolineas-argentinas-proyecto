# Utilitarias


def diccionario():
    return {
    "opcion": validarOpcion,
    "leerArchivo": leerArchivo,
    "agregarArchivo": agregarArchivo,
    "escribirArchivo": escribirArchivo,
    "entero": validarInt,
    "validarOpcionDict": validarOpcionDict,
    "validarDia": validarDia,
    "validarMes": validarMes,
    "validarAno": validarAno,
    "crearArchivo": crearArchivo,
    "validarNombre": validarNombre,
    "manejoNombre" : manejoNombre
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
        archivo = open(nombre, "ab")
        archivo = open("recursos_humanos/" + nombre, "ab")
        return archivo
    except FileNotFoundError:
        print("Objet-File: Archivo no encontrado. ")
        return None


def escribirArchivo(ruta):
    archivo = object
    try:
        archivo = open(ruta, "wb")
        return archivo
    except FileNotFoundError:
        print("Object-File: Archivo no encontrado. ")
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


def validarOpcionDict(opcion, diccionario):
    while True:
        try:
            opcion = int(opcion)
            if  1 <= opcion <= (len(diccionario) + 1):
                return opcion
            opcion = input("Ingrese una opción válida: ")
        except ValueError:
            print("Value Error: The data could not be converted to integer.")
            opcion = input("Ingrese una opción válida: ")
            
            
def validarDia(dia):
    while True:
        dia = validarInt(dia)
        if 1 <= dia <= 31:
            return dia 
        dia = input("Ingrese un día válido: ")


def validarMes(mes):
    while True:
        mes = validarInt(mes)
        if 1 <= mes <= 12:
            return mes 
        mes = input("Ingrese un mes válido: ")
        

def validarAno(ano):
    while True:
        ano = validarInt(ano)
        if ano >= 1950:
            return ano 
        ano = input("Ingrese un año válido: ")
    
    
def crearArchivo(nombre): # archivo .txt
    contador = 1
    while True:
        try:
            archivo = object # objeto
            archivo = open("{}.txt".format(nombre), "x")
            return archivo
        except FileExistsError:
            nombre += "({})".format(contador)
            contador += 1
        


def validarNombre(nombre):
    tupla = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ","@", "#", "$",
             "!", "%", "&", ".", ",", ":", ";", "*", "+", "-", "_", "¿", "?", "¡")
    for i in range(len(nombre)):
        for j in range(len(tupla)):
            if nombre[i] == tupla [j]:
                    return False
    return True

def manejoNombre(nombre):                    
    while True:
        if (validarNombre(nombre) == False):
            nombre = input("Ingrese un nombre o apellido válido: ")
        else:
            return nombre


validar = diccionario()
