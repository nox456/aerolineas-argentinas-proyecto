from .utilitarias_pg import validar
from .desarrollo_pg import solucion


def menuPagos():
    opcion = 0 # int
    cantidad = [] # arreglo uni int
    archivo = object
    pagos = [] # arreglo uni str
    noPagados = [] # arreglo uni str
    print("\n**** PAGOS ****\n")
    print("1. Listar pagos")
    print("2. Pagar")
    print("---------------------------------")
    print("3. SALIR DEL PROGRAMA\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-3): "))
    if opcion == 1:
        archivo = validar["leerArchivo"]("pagos.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        pagos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, pagos)
        solucion["listar"](pagos)
        archivo.close()
    elif opcion == 2:
        archivo = validar["leerArchivo"]("pagos.bin")
        if archivo == None:
            return
        cantidad = solucion["cantidadReg"](archivo)
        pagos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, pagos)
        solucion["registrosNoPagados"](pagos, noPagados)
        solucion["pagar"](noPagados, pagos)
    elif opcion == 3:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")
