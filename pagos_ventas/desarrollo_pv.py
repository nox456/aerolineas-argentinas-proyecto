def diccionario():
    return {
        "cantidadReg": cantidadReg,
        "iniMatriz": iniMatriz,
        "obtenerRegistros": obtenerRegistros,
        "listarPagos": listarPagos,
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


def listarPagos(matriz):
    print("\n-REGISTRO DE PAGOS")
    print("----------------------------------------------")
    if len(matriz) > 0:
        print("{0:10}{1:15}{2:10}{3:9}".format("Tipo", "Nombre", "Precio", "Estado"))
        for i in range(len(matriz)):
            print(
                "{0:10}{1:15}{2:8.2f}  {3:9}".format(
                    matriz[i][0], matriz[i][1], float(matriz[i][2]), matriz[i][3]
                ),
                end="",
            )
    else:
        print("No hay registros de pagos...")
    print("----------------------------------------------")


solucion = diccionario()
