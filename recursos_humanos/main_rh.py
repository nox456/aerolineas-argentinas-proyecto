from .utilitarias_rh import validar
from .desarrollo_rh import recursos_humanos


def menuRecursosHumanos():  # void
    opcion = 0  # int
    print("\n**** RECURSOS HUMANOS ****\n")
    print("1. Listar empleados")
    print("2. Agregar empleado al registro")
    print("3. Elimnar empleado al registro")
    print("4. Crear nómina de empleado")
    print("---------------------------------")
    print("5. SALIR DEL PROGRAMA\n")
    
    opcion = validar["opcion"](input("Ingrese una opción del menú (1-5): "))
    
    if opcion == 1:
        archivo = validar["leerArchivo"]("recursos_humanos/personal.bin")
        recursos_humanos["listar"](archivo)
        archivo.close()
    elif opcion == 2:
        archivoEmpleados = validar["agregarArchivo"]("recursos_humanos/personal.bin")
        archivoRoles = validar["leerArchivo"]("recursos_humanos/roles.bin")
        recursos_humanos["agregar"](archivoEmpleados, archivoRoles)
        archivoEmpleados.close()
        archivoRoles.close()
    elif opcion == 3:
        print("eliminar")
    elif opcion == 4:
        print("nomina")
    elif opcion == 5:
        print("GRACIAS POR USAR EL SOFTWARE!")
    else:
        print("ERROR: Opción no válida!")


