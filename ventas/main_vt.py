from .utilitarias_vt import validar
from .desarrollo_vt import solucion


def menuVentas():
    opcion = 0  # int
    cantidad = [] # arreglo uni int
    ventas = [] # arreglo bi str
    noVendidos = [] # arreglo bi str
    archivo = object
    print("\n**** VENTAS ****\n")
    print("1. Listar ventas")
    print("2. Concretar venta")
    print("---------------------------------")
    print("3. SALIR DEL PROGRAMA\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-3): "))
    if opcion == 1:
        archivo = validar["leerArchivo"]("ventas.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        ventas = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, ventas)
        solucion["listar"](ventas)
    elif opcion == 2:
        archivo = validar["leerArchivo"]("ventas.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        ventas = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, ventas)
        solucion["registrosNoVendidos"](ventas, noVendidos)
        solucion["vender"](noVendidos, ventas)
    elif opcion == 3:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")
