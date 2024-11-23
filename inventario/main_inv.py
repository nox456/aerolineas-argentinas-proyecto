from .utilitarias_inv import validar
from .desarrollo_inv import solucion

def menuInventario():  # void
    opcion = 0  # int
    print("\n**** INVENTARIO ****\n")
    print("1. Listar artículos")
    print("2. Agregar artículos")
    print("3. Eliminar artículos")
    print("---------------------------------")
    print("4. SALIR DEL PROGRAMA\n")
    opcion = validar["validarOpcion"](input("Ingrese una opción del menú (1-4): "))

    if opcion == 1:
        archivo = validar["leerArchivo"]("inventario/articulos.txt")
        solucion["listar"](archivo)
        archivo.close()
    elif opcion == 2:
        archivo = validar["agregarArchivo"]("inventario/articulos.txt")
        solucion["agregar"](archivo)
        archivo.close()
    elif opcion == 3:
        print("eliminar")
    elif opcion == 4:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")

