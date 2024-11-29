from .utilitarias_inv import validar


def diccionario():
    return {
        "listar": listar,
        "registrarPago": registrarPago,
        "registrarVenta": registrarVenta,
        "cantidadReg": cantidadReg,
        "iniMatriz": iniMatriz,
        "obtenerRegistros": obtenerRegistros,
        "obtenerRuta": obtenerRuta,
        "obtenerPrecio": obtenerPrecio,
        "obtenerAsientoVuelo": obtenerAsientoVuelo,
    }


def cantidadReg(archivo):  # arreglo uni int
    cant = [0, 0]  # int
    if archivo != None:
        for linea in archivo:
            campos = linea.decode("utf-8").split("#")
            cant[0] += 1
            cant[1] = len(campos)
        archivo.seek(0)
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
            matriz[n] = registro.decode("utf-8").split("#")
            n += 1
    else:
        print("-------------------")
        print("No hay registros...")
        print("-------------------")


def listar(articulos):  # void
    if len(articulos) > 0:
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


def registrarPago(archivo):  # void
    nombre = ""  # str
    cantidad = 0  # int
    precio = 0.0  # float
    if archivo != None:
        print("\n-AGREGAR ARTÍCULOS")
        nombre = input("Ingrese el Nombre del Artículo: ")
        precio = validar["validarFloat"](input("Ingrese el precio: "))
        cantidad = validar["validarInt"](input("Ingrese la cantidad: "))
        archivo.write(
            "Artículo#{0}#{1}#No Pagado\n".format(nombre, cantidad * precio).encode(
                "utf-8"
            )
        )
        print("\n---ARTÍCULO AGREGADO A LA LISTA DE PAGOS---")


def obtenerRuta(rutas):  # string
    n = 0  # int
    k = 0  # int
    if len(rutas) > 0:
        n = 1
        print("\n-LISTA DE RUTAS")
        print("------------------------------------")
        print("   {0:15}  {1:10}".format("Destino", "Precio"))
        for linea in rutas:
            print("{0:>2} {1:15}  {2:6.2f}".format(n, linea[0], float(linea[1])))
            n += 1
        print("------------------------------------")
        k = validar["validarInt"](
            input("Ingrese la ruta del viaje (1-" + str(n - 1) + "): ")
        )
        while k > (n - 1):
            print("ERROR: Opción fuera de rango")
            k = validar["validarInt"](
                input("Ingrese la ruta del viaje (1-" + str(n - 1) + "): ")
            )
    return rutas[k - 1][0]


def obtenerPrecio(rutas, ruta):  # float
    precio = 0.0  # float
    if len(rutas) > 0:
        for i in range(len(rutas)):
            if rutas[i][0] == ruta:
                precio = float(rutas[i][1])
    return precio


def obtenerAsientoVuelo(asientos):  # arreglo uni int
    f = 0  # int
    c = 0  # int
    asiento = [0, 0]  # str
    if len(asientos) > 0:
        print("\n-LISTA DE ASIENTOS DISPONIBLES")
        print("------------------------------------")
        print("       Asiento   Asiento   Asiento   Asiento")
        for fila in asientos:
            print(
                "{0:5}     {1:2}        {2:2}        {3:2}        {4:2}".format(
                    fila[0], fila[1], fila[2], fila[3], fila[4]
                )
            )
        f = validar["validarInt"](input("Ingrese la fila: "))
        c = validar["validarInt"](input("Ingrese el asiento: "))
        while f > 4 or c > 4:
            print("ERROR: Selección fuera de rango")
            f = validar["validarInt"](input("Ingrese la fila: "))
            c = validar["validarInt"](input("Ingrese el asiento: "))
        asiento[0] = asientos[f - 1][0]
        asiento[1] = asientos[f - 1][c]
        while asiento[1] == "VF":
            print("ERROR: Asiento ya vendido, seleccione otro")
            f = validar["validarInt"](input("Ingrese la fila: "))
            c = validar["validarInt"](input("Ingrese el asiento: "))
            asiento[0] = asientos[f - 1][0]
            asiento[1] = asientos[f - 1][c]
    return asiento


def registrarVenta(archivo, asiento, ruta, precio):  # void
    if archivo != None:
        archivo.write(
            "Boleto#{0}-{1}-{2}#{3:.2f}#No Vendido\n".format(
                ruta, asiento[0], asiento[1], precio
            ).encode("utf-8")
        )
        print("\n---BOLETO AGREGADO A LA LISTA DE VENTAS---")


solucion = diccionario()
