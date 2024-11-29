from .utilitarias_inv import validar
from .desarrollo_inv import solucion


def menuInventario():  # void
    opcion = 0  # int
    archivo = object
    cantidad = []  # arreglo uni int
    articulos = []  # arreglo bi str
    rutas = []  # arreglo bi str
    ruta = ""  # string
    precio = 0.0  # float
    asientos = []  # arreglo bi str
    asiento = ""  # str
    avion = "" # str
    aviones = [] # arreglo uni str
    print("\n**** INVENTARIO ****\n")
    print("1. Listar artículos")
    print("2. Listar asientos")
    print("3. Agregar artículo (Comprar)")
    print("4. Vender boletos")
    print("---------------------------------")
    print("5. SALIR DEL PROGRAMA\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-5): "))

    if opcion == 1:
        archivo = validar["leerArchivo"]("articulos.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        articulos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, articulos)
        solucion["listar"](articulos)
    elif opcion == 2:
        archivo = validar["leerArchivo"]("rutas.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        rutas = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, rutas)
        avion = solucion["obtenerAvion"](rutas)
        if avion == "Estados Unidos":
            archivo = validar["leerArchivo"]("avionEU.bin")
        elif avion == "Venezuela":
            archivo = validar["leerArchivo"]("avionVE.bin")
        elif avion == "México":
            archivo = validar["leerArchivo"]("avionME.bin")
        elif avion == "Colombia":
            archivo = validar["leerArchivo"]("avionCO.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        asientos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, asientos)
        solucion["mostrarAsientos"](asientos)
    elif opcion == 3:
        archivo = validar["agregarArchivo"]("pagos/pagos.bin")
        if archivo == None:
            return
        solucion["registrarPago"](archivo)
        archivo.close()
    elif opcion == 4:
        archivo = validar["leerArchivo"]("rutas.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        rutas = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, rutas)
        ruta = solucion["obtenerRuta"](rutas)
        precio = solucion["obtenerPrecio"](rutas, ruta)
        archivo.close()
        if ruta == "Estados Unidos":
            archivo = validar["leerArchivo"]("avionEU.bin")
        elif ruta == "Venezuela":
            archivo = validar["leerArchivo"]("avionVE.bin")
        elif ruta == "México":
            archivo = validar["leerArchivo"]("avionME.bin")
        elif ruta == "Colombia":
            archivo = validar["leerArchivo"]("avionCO.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        asientos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, asientos)
        asiento = solucion["obtenerAsientoVuelo"](asientos)
        archivo.close()
        archivo = validar["agregarArchivo"]("ventas/ventas.bin")
        if archivo == None:
            return
        solucion["registrarVenta"](archivo, asiento, ruta, precio)
        archivo.close()
    elif opcion == 5:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")
