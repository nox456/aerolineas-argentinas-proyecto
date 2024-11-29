from .utilitarias_vt import validar
from inventario.desarrollo_inv import solucion as solucion_inv


def diccionario():
    return {
        "cantidadReg": cantidadReg,
        "iniMatriz": iniMatriz,
        "obtenerRegistros": obtenerRegistros,
        "listar": listar,
        "registrosNoVendidos": registrosNoVendidos,
        "vender": vender,
    }


def cantidadReg(archivo):  # arreglo uni int
    cant = [0, 0]  # int
    if archivo != None:
        for linea in archivo:
            campos = linea.decode("utf-8").split("#")
            cant[0] += 1
            cant[1] = len(campos)
        archivo.seek(0)
    return cant


def iniMatriz(cant):  # arreglo bi
    if cant[0] > 0 and cant[1] > 0:
        return [["e"] * cant[1] for i in range(cant[0])]
    else:
        return []


def obtenerRegistros(archivo, matriz):  # void
    n = 0  # int
    if archivo != None and len(matriz) > 0:
        for registro in archivo:
            matriz[n] = registro.decode("utf-8").split("#")
            n += 1
        archivo.seek(0)
    else:
        print("-------------------")
        print("No hay registros...")
        print("-------------------")


def listar(ventas):  # void
    if len(ventas) > 0:
        print("\n-LISTA DE VENTAS")
        print("----------------------------------------------------------------")
        print(
            "{0:10} {1:25} {2:12} {3:15}".format(
                "Tipo", "Descripción", "Precio", "Estado"
            )
        )
        for linea in ventas:
            print(
                "{0:10} {1:25} {2:10.2f} $ {3:8}".format(
                    linea[0], linea[1], float(linea[2]), linea[3]
                ),
                end="",
            )
        print("----------------------------------------------------------------")


def registrosNoVendidos(ventas, noVendidos):  # void
    if len(ventas) > 0 and len(noVendidos) == 0:
        for i in range(len(ventas)):
            if ventas[i][3].strip() == "No Vendido":
                noVendidos.append(ventas[i])


def vender(noVendidos, ventas):  # void
    reg = 0  # int
    n = 0  # int
    monto = 0.0  # float
    abono = 0.0  # float
    restante = 0.0  # float
    if len(noVendidos) > 0 and len(ventas) > 0:
        print("\n-REGISTROS SIN VENDER")
        for i in range(len(noVendidos)):
            n += 1
            print(
                "{0}. {1} - {2} - {3:.2f} $".format(
                    n, noVendidos[i][0], noVendidos[i][1], float(noVendidos[i][2])
                )
            )
        reg = validar["validarInt"](input("Ingrese el registro (1-" + str(n) + "): "))
        while reg < 1 or reg > n:
            print("ERROR: Selección fuera de rango!")
            reg = validar["validarInt"](
                input("Ingrese el registro (1-" + str(n) + "): ")
            )
        monto = float(noVendidos[reg - 1][2])
        nombre = noVendidos[reg - 1][1]
        tipo = noVendidos[reg - 1][0]
        abono = validar["validarFloat"](input("Ingrese el abono: "))
        archivo = validar["escribirArchivo"]("ventas.bin")
        if abono < monto:
            restante = monto - abono
            for i in range(len(ventas)):
                if ventas[i][1] == nombre:
                    archivo.write(
                        "{0}#{1}#{2}#No Vendido\n".format(
                            ventas[i][0], nombre, restante
                        ).encode("utf-8")
                    )
                else:
                    archivo.write(
                        "{0}#{1}#{2}#{3}\n".format(
                            ventas[i][0],
                            ventas[i][1],
                            ventas[i][2],
                            ventas[i][3].strip(),
                        ).encode("utf-8")
                    )
            print("--- ABONO REALIZADO ---")
            print("Falta: " + str(restante) + " $")
        elif abono > monto:
            restante = abono - monto
            for i in range(len(ventas)):
                if ventas[i][1] == nombre:
                    archivo.write(
                        "{0}#{1}#{2}#Vendido\n".format(ventas[i][0], nombre, 0).encode(
                            "utf-8"
                        )
                    )
                else:
                    archivo.write(
                        "{0}#{1}#{2}#{3}\n".format(
                            ventas[i][0],
                            ventas[i][1],
                            ventas[i][2],
                            ventas[i][3].strip(),
                        ).encode("utf-8")
                    )
            print("--- ABONO REALIZADO ---")
            print("--- BOLETO VENDIDO ---")
            solucion_inv["boletoVendido"](nombre.split("-")[0],nombre.split("-")[1], nombre.split("-")[2])
            print("Devolución al usuario: " + str(restante) + " $")
        else:
            for i in range(len(ventas)):
                if ventas[i][1] == nombre:
                    archivo.write(
                        "{0}#{1}#{2}#Vendido\n".format(ventas[i][0], nombre, 0).encode(
                            "utf-8"
                        )
                    )
                else:
                    archivo.write(
                        "{0}#{1}#{2}#{3}\n".format(
                            ventas[i][0],
                            ventas[i][1],
                            ventas[i][2],
                            ventas[i][3].strip(),
                        ).encode("utf-8")
                    )
            print("--- ABONO REALIZADO ---")
            print("--- BOLETO VENDIDO ---")
            solucion_inv["boletoVendido"](nombre.split("-")[0],nombre.split("-")[1], nombre.split("-")[2])


solucion = diccionario()
