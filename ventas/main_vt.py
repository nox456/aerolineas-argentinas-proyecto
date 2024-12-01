from .utilitarias_vt import validar
from .desarrollo_vt import solucion


def menuVentas():
    opcion = 0  # int
    cantidad = []  # arreglo uni int
    ventas = []  # arreglo bi str
    vencidas = []  # arreglo uni str
    noVendidos = []  # arreglo bi str
    fecha_actual = []  # arreglo uni int
    archivo = object
    print("\n**** VENTAS ****\n")
    print("1. Listar ventas")
    print("2. Concretar venta")
    print("3. Renovar venta")
    print("4. Cancelar venta")
    print("---------------------------------")
    print("5. SALIR DEL PROGRAMA\n")
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
        archivo = validar["leerArchivo"]("ventas.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        ventas = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, ventas)
        fecha_actual = solucion["registrosVencidos"](ventas, vencidas)
        solucion["mostrarVencidos"](vencidas, fecha_actual)
        archivo = validar["escribirArchivo"]("ventas.bin")
        if archivo == None:
            return
        solucion["renovarVenta"](ventas, vencidas, fecha_actual, archivo)
    elif opcion == 5:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")
