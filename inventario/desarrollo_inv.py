def diccionario():
    return {"listar": listar}


def listar(archivo):
    if archivo != None:
        print("-----------------------")
        print("{0:12}{1:3}".format("Nombre", "Cantidad"))
        for fila in archivo:
            campos = fila.decode("utf-8").split("#")
            print("{0:15}{1:3}".format(campos[0], int(campos[1])))
        print("-----------------------")


solucion = diccionario()
