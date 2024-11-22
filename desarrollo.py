from recursos_humanos.main_rh import menuRecursosHumanos
from validaciones import validar
from inventario.main_inv import menuInventario


def diccionario():
    return {
        "menuPrincipal": menuPrincipal,
        "menuRecursosHumanos": menuRecursosHumanos,
        "menuInventario": menuInventario,
    }


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
    return validar["opcion"](input("Ingrese una opción del menú (1-5): "))


solucion = diccionario()

