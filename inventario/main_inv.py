from .utilitarias_inv import validar
from .desarrollo_inv import solucion


def menuInventario():  # void
    opcion = 0  # int
    archivo = object
    cantidad = []  # arreglo uni int
    articulos = []  # arreglo bi str
    print("\n**** INVENTARIO ****\n")
    print("1. Listar artículos")
    print("2. Agregar artículo (Comprar)")
    print("---------------------------------")
    print("3. SALIR DEL PROGRAMA\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-3): "))

    if opcion == 1:
        archivo = validar["leerArchivo"]("articulos.txt")
        cantidad = solucion["cantidadReg"](archivo)
        archivo.seek(0)
        articulos = solucion["iniMatriz"](cantidad)
        solucion["obtenerRegistros"](archivo, articulos)
        solucion["listar"](articulos)
        archivo.close()
    elif opcion == 2:
        archivo = validar["agregarArchivo"]("pagos.txt")
        solucion["agregar"](archivo)
        archivo.close()
    elif opcion == 3:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")
