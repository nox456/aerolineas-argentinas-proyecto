from desarrollo import solucion


def main():
    opcion = 0  # int

    opcion = solucion["menuPrincipal"]()

    if opcion == 1:
        solucion["menuRecursosHumanos"]()
    elif opcion == 2:
        solucion["menuPagos"]()
    # IMPLEMENTACIÓN DEL MÓDULO DE VENTAS
    # elif opcion == 3:
    #     solucion["menuVentas"]()
    elif opcion == 3:
        solucion["menuInventario"]()
    elif opcion == 4:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")


main()
