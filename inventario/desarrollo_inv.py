from .utilitarias_inv import validar

def diccionario():
    return {"listar": listar, "agregar": agregar}


def listar(archivo):
    if archivo != None:
        print("\n-LISTA DE ARTÍCULOS")
        print("------------------------------------")
        print("{0:12}{1:3}  {2:6}".format("Nombre", "Cantidad", "Precio Total"))
        for fila in archivo:
            campos = fila.decode("utf-8").split("#")
            print(
                "{0:15}{1:3}     {2:.2f} $".format(
                    campos[0], int(campos[1]), float(campos[2])
                )
            )
        print("------------------------------------")


def agregar(archivo): # void
    nombre = ""  # str
    cantidad = 0  # int
    precio = 0.0  # float
    if archivo != None:
        print("\n-AGREGAR ARTÍCULOS")
        nombre = input("Ingrese el Nombre del Artículo: ")
        cantidad = validar["validarInt"](input("Ingrese la cantidad: "))
        precio = validar["validarFloat"](input("Ingrese el precio total: "))
        archivo.write("{0}#{1}#{2}\n".format(nombre, cantidad, precio))
        print("\n---ARTÍCULO AGREGADO---")


solucion = diccionario()
