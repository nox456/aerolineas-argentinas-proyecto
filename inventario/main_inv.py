from .utilitarias_inv import validar
from .desarrollo_inv import solucion


def menuInventario():  # void
    opcion = 0  # int
    archivo = object
    cantidad = []  # arreglo uni int
    articulos = []  # arreglo bi str
    rutas = []  # arreglo bi str
    precio = 0.0 # float
    asientos = [] # arreglo bi str
    asiento = "" # str
    print("\n**** INVENTARIO ****\n")
    print("1. Listar artículos")
    print("2. Agregar artículo (Comprar)")
    print("3. Vender boletos")
    print("---------------------------------")
    print("4. SALIR DEL PROGRAMA\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-4): "))

    if opcion == 1:
        archivo = validar["leerArchivo"]("articulos.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        articulos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, articulos)
        solucion["listar"](articulos)
    elif opcion == 2:
        print("FALTA IMPLEMENTACIÓN DE AGREGAR UN REGISTRO AL MÓDULO DE PAGOS")
        # archivo = validar["agregarArchivo"]("pagos/pagos.bin")
        # if archivo == None:
        #     return
        # solucion["agregar"](archivo)
        archivo.close()
    elif opcion == 3:
        archivo = validar["leerArchivo"]("rutas.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        rutas = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, rutas)
        precio = solucion["obtenerPrecioRuta"](rutas)
        archivo.close()
        archivo = validar["leerArchivo"]("avion.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        asientos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, asientos)
        asiento = solucion["obtenerAsientoVuelo"](asientos)
        archivo.close()
        print("FALTA IMPLEMENTACIÓN DE AGREGAR UN REGISTRO AL MÓDULO DE VENTAS")
        # archivo = validar["agregarArchivo"]("ventas/ventas.bin")
        # if archivo == None:
        #     return
        # solucion["registrarVenta"](archivo, asiento, precio)
        # archivo.close()
    elif opcion == 4:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")
