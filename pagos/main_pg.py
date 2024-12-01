from .utilitarias_pg import validar
from .desarrollo_pg import solucion


def menuPagos():
    opcion = 0  # int
    cantidad = []  # arreglo uni int
    archivo = object
    pagos = []  # arreglo uni str
    noPagados = []  # arreglo uni str
    vencidos = []  # arreglo uni str
    fecha_actual = []  # arreglo uni int
    print("\n**** PAGOS ****\n")
    print("1. Listar pagos")
    print("2. Pagar")
    print("3. Renovar pago")
    print("4. Cancelar pago")
    print("---------------------------------")
    print("5. MENU PRINCIPAL\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-5): "))
    while True:
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
            archivo = validar["leerArchivo"]("pagos.bin")
            if archivo == None:
                return
            cantidad = solucion["cantidadReg"](archivo)
            pagos = solucion["iniMatriz"](cantidad)
            solucion["obtenerRegistros"](archivo, pagos)
            fecha_actual = solucion["registrosVencidos"](pagos, vencidos)
            solucion["mostrarVencidos"](vencidos, fecha_actual)
            archivo = validar["escribirArchivo"]("pagos.bin")
            if archivo == None:
                return
            solucion["renovarPago"](pagos, vencidos, fecha_actual, archivo)
        elif opcion == 4:
            archivo = validar["leerArchivo"]("pagos.bin")
            if archivo == None:
                return
            cantidad = solucion["cantidadReg"](archivo)
            pagos = solucion["iniMatriz"](cantidad)
            solucion["obtenerRegistros"](archivo, pagos)
            solucion["registrosNoPagados"](pagos, noPagados)
            archivo = validar["escribirArchivo"]("pagos.bin")
            if archivo == None:
                return
            solucion["cancelarPago"](pagos, noPagados, archivo)
        elif opcion == 5:
            return
        else:
            print("ERROR: Opción no válida!")
        opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-5): "))
