from .utilitarias_inv import validar


def diccionario():
    return {
        "listar": listar,
        "agregar": agregar,
        "cantidadReg": cantidadReg,
        "iniMatriz": iniMatriz,
        "obtenerRegistros": obtenerRegistros,
    }


def cantidadReg(archivo):  # arreglo uni int
    cant = [0, 0]  # int
    if archivo != None:
        for linea in archivo:
            campos = linea.split("#")
            cant[0] += 1
            cant[1] = len(campos)
    return cant


def iniMatriz(cant):  # arreglo bi
    if cant[0] > 0 and cant[1] > 0:
        return [["e"] * cant[1] for i in range(cant[0])]
    else:
        return []


def obtenerRegistros(archivo, matriz):  # void
    n = 0  # int
    if archivo != None and len(matriz) > 0:
        for registro in archivo:
            matriz[n] = registro.split("#")
            n += 1


def listar(articulos):  # void
    if len(articulos):
        print("\n-LISTA DE ARTÍCULOS")
        print("------------------------------------")
        print("{0:12}{1:3}  {2:6}".format("Nombre", "Cantidad", "Precio Total"))
        for linea in articulos:
            print(
                "{0:15}{1:3}     {2:.2f} $".format(
                    linea[0], int(linea[1]), float(linea[2])
                )
            )
        print("------------------------------------")


def agregar(archivo):  # void
    nombre = ""  # str
    cantidad = 0  # int
    precio = 0.0  # float
    if archivo != None:
        print("\n-AGREGAR ARTÍCULOS")
        nombre = input("Ingrese el Nombre del Artículo: ")
        precio = validar["validarFloat"](input("Ingrese el precio: "))
        cantidad = validar["validarInt"](input("Ingrese la cantidad: "))
        archivo.write("Artículo#{0}#{1}#No Pagado\n".format(nombre, cantidad * precio))
        print("\n---ARTÍCULO AGREGADO A LA LISTA DE PAGOS---")


solucion = diccionario()
