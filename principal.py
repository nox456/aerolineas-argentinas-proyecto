from desarrollo import solucion


def main():
    opcion = 0  # int

    opcion = solucion["menuPrincipal"]()

    if opcion == 1:
        solucion["menuRecursosHumanos"]()
    # IMPLEMENTACIÓN DEL MÓDULO DE PAGOS
    # elif opcion == 2:
    #     solucion["menuPagos"]()
    # IMPLEMENTACIÓN DEL MÓDULO DE VENTAS
    # elif opcion == 3:
    #     solucion["menuVentas"]()
    elif opcion == 2:
        solucion["menuInventario"]()
    elif opcion == 3:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")


main()
