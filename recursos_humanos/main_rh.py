from .utilitarias_rh import validar
from .desarrollo_rh import solucion
from inventario.desarrollo_inv import solucion as solucion_inv
from ventas.desarrollo_vt import solucion as solucion_vt


def menuRecursosHumanos():  # void
    opcion = 0  # int
    archivo = object
    cantidad = []  # arreglo uni int
    empleados = []  # arreglo bi str
    roles = []  # arreglo bi str
    rutas = []  # arreglo bi str
    razon = ""  # string
    monto = 0.0  # float
    venta = ""  # str
    print("\n**** RECURSOS HUMANOS ****\n")
    print("1. Listar empleados")
    print("2. Agregar empleado al registro")
    print("3. Liquidación")
    print("4. Crear nómina de empleado")
    print("5. Cancelar Vuelo")
    print("---------------------------------")
    print("6. MENU PRINCIPAL\n")

    opcion = validar["opcion"](input("Ingrese una opción del menú (1-6): "))

    while True:
        if opcion == 1:
            archivo = validar["leerArchivo"]("recursos_humanos/personal.bin")
            if archivo == None:
                return
            cantidad = solucion["cantidadReg"](archivo)
            empleados = solucion["iniMatriz"](cantidad)
            solucion["obtenerRegistros"](archivo, empleados)
            solucion["listar"](empleados)
        elif opcion == 2:
            archivo = validar["leerArchivo"]("recursos_humanos/roles.bin")
            if archivo == None:
                return
            cantidad = solucion["cantidadReg"](archivo)
            roles = solucion["iniMatriz"](cantidad)
            solucion["obtenerRegistros"](archivo, roles)
            archivo.close()
            archivo = validar["agregarArchivo"]("recursos_humanos/personal.bin")
            if archivo == None:
                return
            solucion["agregar"](archivo, roles)
            archivo.close()
        elif opcion == 3:
            solucion["liquidacion"]()
        elif opcion == 4:
            archivo = validar["leerArchivo"]("recursos_humanos/personal.bin")
            if archivo == None:
                return
            cantidad = solucion["cantidadReg"](archivo)
            empleados = solucion["iniMatriz"](cantidad)
            solucion["obtenerRegistros"](archivo, empleados)
            archivo = validar["leerArchivo"]("recursos_humanos/personal.bin")
            if archivo == None:
                return
            solucion["nomina"](archivo, empleados)
        elif opcion == 5:
            archivo = validar["leerArchivo"]("inventario/rutas.bin")
            if archivo == None:
                return
            cantidad = solucion["cantidadReg"](archivo)
            rutas = solucion["iniMatriz"](cantidad)
            solucion["obtenerRegistros"](archivo, rutas)
            avion = solucion_inv["obtenerAvion"](rutas)
            razon = solucion["razonCancelacion"]()
            if razon == "Avion":
                monto = solucion_inv["devolverDineroTodo"](avion, rutas)
                solucion_inv["devolverAsientos"](avion)
                solucion_vt["eliminarRegistroAvion"](avion)
                print("--- DEVOLUCIÓN FINALIZADA ---")
                print("Dinero devuelto: {:.2f} $".format(monto))
            elif razon == "Pasajero":
                venta = solucion_inv["devolverDinero"](avion)
                solucion_vt["eliminarRegistro"](venta)
        elif opcion == 6:
            return
        else:
            print("ERROR: Opción no válida!")
        opcion = validar["opcion"](input("Ingrese una opción del menú (1-5): "))
