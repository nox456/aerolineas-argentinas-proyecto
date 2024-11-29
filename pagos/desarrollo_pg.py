from .utilitarias_pg import validar
from recursos_humanos.desarrollo_rh import solucion as solucion_rh
from inventario.desarrollo_inv import solucion as solucion_inv


def diccionario():
    return {
        "cantidadReg": cantidadReg,
        "iniMatriz": iniMatriz,
        "obtenerRegistros": obtenerRegistros,
        "listar": listar,
        "registrosNoPagados": registrosNoPagados,
        "pagar": pagar,
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


def listar(pagos):  # void
    if len(pagos) > 0:
        print("\n-LISTA DE PAGOS")
        print("--------------------------------------------------")
        print(
            "{0:15} {1:15} {2:14} {3:8}".format(
                "Tipo", "Descripción", "Precio", "Estado"
            )
        )
        for linea in pagos:
            if linea[0] == "Liq. Despido" or linea[0] == "Liq. Renuncia":
                print(
                    "{0:15} {1:15} {2:12.2f} $ {3:5}".format(
                        linea[0],
                        "-".join(linea[1].split("-")[0:2]),
                        float(linea[2]),
                        linea[3],
                    ),
                    end="",
                )
            else:
                print(
                    "{0:15} {1:15} {2:12.2f} $ {3:5}".format(
                        linea[0], linea[1].split("-")[0], float(linea[2]), linea[3]
                    ),
                    end="",
                )
        print("--------------------------------------------------")


def registrosNoPagados(pagos, noPagados):  # void
    if len(pagos) > 0 and len(noPagados) == 0:
        for i in range(len(pagos)):
            if pagos[i][3].strip() == "No Pagado":
                noPagados.append(pagos[i])


def pagar(noPagados, pagos):  # void
    reg = 0  # int
    n = 0  # int
    monto = 0.0  # float
    abono = 0.0  # float
    restante = 0.0  # float
    nombre = ""  # string
    articulo = ""  # string
    cantidad = 0  # int
    tipo = ""  # string
    datos = []  # arreglo uni string
    calculos = []  # arreglo uni float
    fecha_actual = []  # arreglo uni int
    dias_antiguedad = 0.0  # float
    archivo = object
    if len(noPagados) > 0 and len(pagos) > 0:
        print("\n-REGISTROS SIN PAGAR")
        for i in range(len(noPagados)):
            n += 1
            if noPagados[i][0] == "Liq. Despido" or noPagados[i][0] == "Liq. Renuncia":
                print(
                    "{0}. {1} - {2} - {3:.2f} $".format(
                        n,
                        noPagados[i][0],
                        "-".join(noPagados[i][1].split("-")[0:2]),
                        float(noPagados[i][2]),
                    )
                )
            else:
                print(
                    "{0}. {1} - {2} - {3:.2f} $".format(
                        n,
                        noPagados[i][0],
                        noPagados[i][1].split("-")[0],
                        float(noPagados[i][2]),
                    )
                )

        reg = validar["validarInt"](input("Ingrese el registro (1-" + str(n) + "): "))
        while reg < 1 or reg > n:
            print("ERROR: Selección fuera de rango!")
            reg = validar["validarInt"](
                input("Ingrese el registro (1-" + str(n) + "): ")
            )
        monto = float(noPagados[reg - 1][2])
        nombre = noPagados[reg - 1][1]
        tipo = noPagados[reg - 1][0]
        abono = validar["validarFloat"](input("Ingrese el abono: "))
        archivo = validar["escribirArchivo"]("pagos.bin")
        if abono < monto:
            restante = monto - abono
            for i in range(len(pagos)):
                if pagos[i][1] == nombre:
                    archivo.write(
                        "{0}#{1}#{2}#No Pagado\n".format(
                            pagos[i][0], nombre, restante
                        ).encode("utf-8")
                    )
                else:
                    archivo.write(
                        "{0}#{1}#{2}#{3}\n".format(
                            pagos[i][0], pagos[i][1], pagos[i][2], pagos[i][3].strip()
                        ).encode("utf-8")
                    )

            print("--- ABONO REALIZADO ---")
            print("Falta: " + str(restante) + " $")
        elif abono > monto:
            restante = abono - monto
            for i in range(len(pagos)):
                if pagos[i][1] == nombre:
                    archivo.write(
                        "{0}#{1}#{2}#Pagado\n".format(pagos[i][0], nombre, 0).encode(
                            "utf-8"
                        )
                    )
                else:
                    archivo.write(
                        "{0}#{1}#{2}#{3}\n".format(
                            pagos[i][0], pagos[i][1], pagos[i][2], pagos[i][3].strip()
                        ).encode("utf-8")
                    )
            print("--- ABONO REALIZADO ---")
            if tipo == "Artículo":
                articulo = nombre.split("-")[0]
                cantidad = int(nombre.split("-")[1])
                solucion_inv["agregar"](articulo, cantidad)
                print("--- ARTÍCULO PAGADO Y AGREGADO AL INVENTARIO ---")
            elif tipo == "Liq. Despido":
                datos = nombre.split("-")[0:10]
                fecha_actual = nombre.split("-")[10:13]
                dias_antiguedad = nombre.split("-")[13]
                calculos = nombre.split("-")[14:27]
                solucion_rh["generarArchivoDespido"](
                    datos, calculos, fecha_actual, float(dias_antiguedad)
                )
                solucion_rh["eliminarRegistro"](
                    nombre.split("-")[0], nombre.split("-")[1]
                )
                print("--- LIQUIDACIÓN CREADA ---")
            elif tipo == "Liq. Renuncia":
                datos = nombre.split("-")[0:10]
                fecha_actual = nombre.split("-")[10:13]
                dias_antiguedad = nombre.split("-")[13]
                calculos = nombre.split("-")[14:30]
                solucion_rh["generarArchivoRenuncia"](
                    datos, calculos, fecha_actual, float(dias_antiguedad)
                )
                solucion_rh["eliminarRegistro"](
                    nombre.split("-")[0], nombre.split("-")[1]
                )
                print("--- LIQUIDACIÓN CREADA ---")
            print("Devolución al usuario: " + str(restante) + " $")
        else:
            for i in range(len(pagos)):
                if pagos[i][1] == nombre:
                    archivo.write(
                        "{0}#{1}#{2}#Pagado\n".format(pagos[i][0], nombre, 0).encode(
                            "utf-8"
                        )
                    )
                else:
                    archivo.write(
                        "{0}#{1}#{2}#{3}\n".format(
                            pagos[i][0], pagos[i][1], pagos[i][2], pagos[i][3].strip()
                        ).encode("utf-8")
                    )
            print("--- ABONO REALIZADO ---")
            if tipo == "Artículo":
                articulo = nombre.split("-")[0]
                cantidad = int(nombre.split("-")[1])
                solucion_inv["agregar"](articulo, cantidad)
                print("--- ARTÍCULO PAGADO Y AGREGADO AL INVENTARIO ---")
            elif tipo == "Liq. Despido":
                datos = nombre.split("-")[0:10]
                fecha_actual = nombre.split("-")[10:13]
                dias_antiguedad = nombre.split("-")[13]
                calculos = nombre.split("-")[14:27]
                solucion_rh["generarArchivoDespido"](
                    datos, calculos, fecha_actual, float(dias_antiguedad)
                )
                solucion_rh["eliminarRegistro"](
                    nombre.split("-")[0], nombre.split("-")[1]
                )
                print("--- LIQUIDACIÓN CREADA ---")
            elif tipo == "Liq. Renuncia":
                datos = nombre.split("-")[0:10]
                fecha_actual = nombre.split("-")[10:13]
                dias_antiguedad = nombre.split("-")[13]
                calculos = nombre.split("-")[14:30]
                solucion_rh["generarArchivoRenuncia"](
                    datos, calculos, fecha_actual, float(dias_antiguedad)
                )
                solucion_rh["eliminarRegistro"](
                    nombre.split("-")[0], nombre.split("-")[1]
                )
                print("--- LIQUIDACIÓN CREADA ---")
    else:
        print("-------------------------------------")
        print("Todos los registros están pagados...")
        print("-------------------------------------")


solucion = diccionario()
