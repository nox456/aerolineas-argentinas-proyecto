from validaciones import validar
from recursos_humanos.desarrollo import recursos_humanos


def menuPrincipal():  # int
    print("*****************************")
    print("*** AEROLÍNEAS ARGENTINAS ***")
    print("*****************************\n")
    print("1. Recursos Humanos")
    print("2. Ventas")
    print("3. Inventario")
    print("4. Almacen")
    print("-----------------------")
    print("5. SALIR DEL PROGRAMA\n")
    return validar["opcion"]()


def menuRecursosHumanos():  # void
    opcion = 0  # int
    print("\n**** RECURSOS HUMANOS ****\n")
    print("1. Listar empleados")
    print("2. Agregar empleado al registro")
    print("3. Elimnar empleado al registro")
    print("4. Crear nómina de empleado")
    print("---------------------------------")
    print("5. SALIR DEL PROGRAMA\n")
    opcion = validar["opcion"]()
    if opcion == 1:
        archivo = validar["abrirArchivo"]("recursos_humanos/personal.bin")
        recursos_humanos["listar"](archivo)
    elif opcion == 2:
        print("agregar")
    elif opcion == 3:
        print("eliminar")
    elif opcion == 4:
        print("nomina")
    elif opcion == 5:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")


solucion = {
    "menuPrincipal": menuPrincipal,
    "menuRecursosHumanos": menuRecursosHumanos,
}
