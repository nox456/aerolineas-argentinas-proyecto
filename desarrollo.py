from recursos_humanos.main_rh import menuRecursosHumanos
from pagos.main_pg import menuPagos
# from ventas.main_vt import menuVentas
from inventario.main_inv import menuInventario
from validaciones import validar


def diccionario():
    return {
        "menuPrincipal": menuPrincipal,
        "menuRecursosHumanos": menuRecursosHumanos,
        "menuPagos": menuPagos,
        # "menuVentas": menuVentas,
        "menuInventario": menuInventario,
    }


def menuPrincipal():  # int
    print("*****************************")
    print("*** AEROLÍNEAS ARGENTINAS ***")
    print("*****************************\n")
    print("1. Recursos Humanos")
    print("2. Pagos")
    # print("3. Ventas")
    print("3. Inventario")
    print("-----------------------")
    print("4. SALIR DEL PROGRAMA\n")
    return validar["opcion"](input("Ingrese una opción del menú (1-4): "))


solucion = diccionario()

