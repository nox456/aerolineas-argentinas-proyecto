from .utilitarias_pv import validar
from .desarrollo_pv import solucion


def menuPagosVentas():  # void
    opcion = 0  # int
    pagos = []  # arreglo bi str
    cantidad = []  # arreglo uni int
    nombreArchivo = ""  # str
    archivo = object
    print("\n**** PAGOS Y VENTAS ****\n")
    print("1. Ver registro de pagos")
    print("2. Realizar Pago")
    print("---------------------------------")
    print("3. SALIR DEL PROGRAMA\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-3): "))
    if opcion == 1:
        nombreArchivo = "pagos.txt"
        archivo = validar["leerArchivo"](nombreArchivo)
        cantidad = solucion["cantidadReg"](archivo)
        archivo.seek(0)
        pagos = solucion["iniMatriz"](cantidad)
        pagos = solucion["obtenerRegistros"](archivo, pagos)
        solucion["listarPagos"](pagos)
    elif opcion == 2:
        print("ventas")
    elif opcion == 3:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")
