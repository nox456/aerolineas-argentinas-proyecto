from validaciones import diccValidaciones


def mostrarMenu():  # void
    print("*****************************")
    print("*** AEROLÍNEAS ARGENTINAS ***")
    print("*****************************\n")
    print("1. Recursos Humanos")
    print("2. Ventas")
    print("3. Inventario")
    print("4. Almacen")
    print("-----------------------")
    print("5. SALIR DEL PROGRAMA\n")


def seleccionMenu():
    opcion = 0  # int
    opcion = diccValidaciones["validarOpcion"](input("Ingrese una opción (1-5): "))
    if opcion == 1:
        print("RH")
    elif opcion == 2:
        print("V")
    elif opcion == 3:
        print("I")
    elif opcion == 4:
        print("A")
    elif opcion == 5:
        print("GRACIAS POR USAR EL SOFTWARE!")


solucion = {"mostrarMenu": mostrarMenu, "seleccionMenu": seleccionMenu}
