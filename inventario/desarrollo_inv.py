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
        "agregar": agregar,
        "boletoVendido": boletoVendido,
        "obtenerAvion": obtenerAvion,
        "mostrarAsientos": mostrarAsientos,
        "devolverAsientos": devolverAsientos,
        "devolverDineroTodo": devolverDineroTodo,
        "devolverDinero": devolverDinero,
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
        print("{0:12}{1:3}".format("Nombre", "Cantidad"))
        for linea in articulos:
            print("{0:15}{1:3}".format(linea[0], int(linea[1])))
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
            "Artículo#{0}-{1}#{2}#No Pagado\n".format(
                nombre, cantidad, cantidad * precio
            ).encode("utf-8")
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
                ruta, asiento[0], asiento[1].strip(), precio
            ).encode("utf-8")
        )
        print("\n---BOLETO AGREGADO A LA LISTA DE VENTAS---")


def agregar(nombre, cantidad):  # void
    archivo = object
    archivo = validar["agregarArchivo"]("inventario/articulos.bin")
    if cantidad > 0 and archivo != None:
        archivo.write("{0}#{1}\n".format(nombre, cantidad).encode("utf-8"))
        archivo.close()


def boletoVendido(avion, fila, asiento):  # void
    archivo = object
    cantidad = []  # arreglo uni int
    asientos = []  # arreglo bi string
    if avion == "Estados Unidos":
        archivo = validar["leerArchivo"]("avionEU.bin")
    elif avion == "Venezuela":
        archivo = validar["leerArchivo"]("avionVE.bin")
    elif avion == "México":
        archivo = validar["leerArchivo"]("avionME.bin")
    elif avion == "Colombia":
        archivo = validar["leerArchivo"]("avionCO.bin")
    cantidad = solucion["cantidadReg"](archivo)
    asientos = solucion["iniMatriz"](cantidad)
    solucion["obtenerRegistros"](archivo, asientos)
    archivo.close()
    if avion == "Estados Unidos":
        archivo = validar["escribirArchivo"]("avionEU.bin")
    elif avion == "Venezuela":
        archivo = validar["escribirArchivo"]("avionVE.bin")
    elif avion == "México":
        archivo = validar["escribirArchivo"]("avionME.bin")
    elif avion == "Colombia":
        archivo = validar["escribirArchivo"]("avionCO.bin")
    if archivo != None:
        for i in range(len(asientos)):
            archivo.write("{0}".format(asientos[i][0]).encode("utf-8"))
            for j in range(1, len(asientos[i])):
                if asientos[i][j].strip() == asiento and asientos[i][0] == fila:
                    archivo.write("#VF".encode("utf-8"))
                else:
                    archivo.write("#{0}".format(asientos[i][j].strip()).encode("utf-8"))
            archivo.write("\n".encode("utf-8"))
        archivo.close()


def obtenerAvion(rutas):  # str
    avion = ""  # str
    n = 0  # int
    k = 0  # int
    if len(rutas) > 0:
        print("\n-LISTA DE AVIONES")
        for i in range(len(rutas)):
            n += 1
            print("{0}. {1}".format(n, rutas[i][0]))
        k = validar["validarInt"](input("Ingrese la opción (1-" + str(n) + "): "))
        while k < 1 or k > n:
            print("ERROR: Opción fuera de rango")
            k = validar["validarInt"](input("Ingrese la opción (1-" + str(n) + "): "))
        avion = rutas[k - 1][0]
    return avion


def mostrarAsientos(asientos):  # void
    if len(asientos) > 0:
        print("\n-LISTA DE ASIENTOS")
        print("-----------------------------------------------")
        print("       Asiento   Asiento   Asiento   Asiento")
        for fila in asientos:
            print(
                "{0:5}     {1:2}        {2:2}        {3:2}        {4:2}".format(
                    fila[0], fila[1], fila[2], fila[3], fila[4]
                )
            )
        print("-----------------------------------------------")


def devolverDineroTodo(avion, rutas):  # float
    monto_final = 0.0  # float
    monto = 0.0  # float
    archivo = object
    for i in range(len(rutas)):
        if rutas[i][0] == avion:
            monto = float(rutas[i][1])
    if avion == "Estados Unidos":
        archivo = validar["leerArchivo"]("avionEU.bin")
    elif avion == "Venezuela":
        archivo = validar["leerArchivo"]("avionVE.bin")
    elif avion == "México":
        archivo = validar["leerArchivo"]("avionME.bin")
    elif avion == "Colombia":
        archivo = validar["leerArchivo"]("avionCO.bin")
    if archivo != None:
        for linea in archivo:
            for campo in linea.decode("utf-8").split("#"):
                if campo == "VF":
                    monto_final += monto
    return monto_final


def devolverAsientos(avion): # arreglo uni str
    f = 0  # int
    c = 0  # int
    archivo = object
    f = 4
    c = 4
    if avion == "Estados Unidos":
        archivo = validar["escribirArchivo"]("avionEU.bin")
    elif avion == "Venezuela":
        archivo = validar["escribirArchivo"]("avionVE.bin")
    elif avion == "México":
        archivo = validar["escribirArchivo"]("avionME.bin")
    elif avion == "Colombia":
        archivo = validar["escribirArchivo"]("avionCO.bin")
    if archivo != None:
        for i in range(f):
            archivo.write("Fila{}".format(i + 1).encode("utf-8"))
            for j in range(c):
                archivo.write("#0{}".format(j + 1).encode("utf-8"))
            archivo.write("\n".encode("utf-8"))

        archivo.close()
    print("--- ASIENTOS LIBERADOS ---")


def devolverDinero(avion):  # str
    fila = 0  # int
    asiento = 0  # int
    asientos = []  # arreglo bi str
    cantidad = []  # arreglo uni int
    rutas = []  # arreglo uni str
    monto = 0.0  # flaot
    archivo = object
    archivo = validar["leerArchivo"]("rutas.bin")
    cantidad = solucion["cantidadReg"](archivo)
    rutas = solucion["iniMatriz"](cantidad)
    solucion["obtenerRegistros"](archivo, rutas)
    if avion == "Estados Unidos":
        archivo = validar["leerArchivo"]("avionEU.bin")
    elif avion == "Venezuela":
        archivo = validar["leerArchivo"]("avionVE.bin")
    elif avion == "México":
        archivo = validar["leerArchivo"]("avionME.bin")
    elif avion == "Colombia":
        archivo = validar["leerArchivo"]("avionCO.bin")
    cantidad = solucion["cantidadReg"](archivo)
    asientos = solucion["iniMatriz"](cantidad)
    solucion["obtenerRegistros"](archivo, asientos)
    archivo.seek(0)
    solucion["mostrarAsientos"](asientos)
    fila = validar["validarInt"](input("Ingrese la fila del pasajero (1-4): "))
    asiento = validar["validarInt"](input("Ingrese el asiento del pasajero (1-4): "))
    while fila > 4 or asiento > 4:
        print("ERROR: Selección fuera de rango")
        fila = validar["validarInt"](input("Ingrese la fila: "))
        asiento = validar["validarInt"](input("Ingrese el asiento: "))
    while asientos[fila - 1][asiento].strip() != "VF":
        print("ERROR: Asiento sin vender! Seleccione otro")
        fila = validar["validarInt"](input("Ingrese la fila: "))
        asiento = validar["validarInt"](input("Ingrese el asiento: "))
        while fila > 4 or asiento > 4:
            print("ERROR: Selección fuera de rango")
            fila = validar["validarInt"](input("Ingrese la fila: "))
            asiento = validar["validarInt"](input("Ingrese el asiento: "))
    if avion == "Estados Unidos":
        archivo = validar["escribirArchivo"]("avionEU.bin")
    elif avion == "Venezuela":
        archivo = validar["escribirArchivo"]("avionVE.bin")
    elif avion == "México":
        archivo = validar["escribirArchivo"]("avionME.bin")
    elif avion == "Colombia":
        archivo = validar["escribirArchivo"]("avionCO.bin")
    for i in range(len(asientos)):
        archivo.write("{}".format(asientos[i][0]).encode("utf-8"))
        for j in range(1, len(asientos[i])):
            if (i + 1) == fila and j == asiento:
                archivo.write("#0{}".format(j).encode("utf-8"))
            else:
                archivo.write("#{}".format(asientos[i][j]).strip().encode("utf-8"))
        archivo.write("\n".encode("utf-8"))
    if avion == "Estados Unidos":
        monto = float(rutas[0][1])
    elif avion == "Venezuela":
        monto = float(rutas[1][1])
    elif avion == "México":
        monto = float(rutas[2][1])
    elif avion == "Colombia":
        monto = float(rutas[3][1])
    print("--- ASIENTOS LIBERADOS ---")
    print("--- DEVOLUCIÓN FINALIZADA ---")
    print("Dinero devuelto: {:.2f} $".format(monto))
    return "{0}-{1}-0{2}".format(avion, asientos[fila - 1][0], asiento)


solucion = diccionario()
