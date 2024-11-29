from desarrollo import solucion


def main():
    opcion = 0  # int

    opcion = solucion["menuPrincipal"]()

    if opcion == 1:
        solucion["menuRecursosHumanos"]()
    elif opcion == 2:
        solucion["menuPagos"]()
    elif opcion == 3:
        solucion["menuVentas"]()
    elif opcion == 4:
        solucion["menuInventario"]()
    elif opcion == 5:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")


main()
