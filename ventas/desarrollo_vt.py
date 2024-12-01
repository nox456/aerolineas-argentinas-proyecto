from .utilitarias_vt import validar
from inventario.desarrollo_inv import solucion as solucion_inv
from recursos_humanos.desarrollo_rh import solucion as solucion_rh


def diccionario():
    return {
        "cantidadReg": cantidadReg,
        "iniMatriz": iniMatriz,
        "obtenerRegistros": obtenerRegistros,
        "listar": listar,
        "registrosNoVendidos": registrosNoVendidos,
        "vender": vender,
        "eliminarRegistroAsiento": eliminarRegistroAsiento,
        "eliminarRegistroAvion": eliminarRegistroAvion,
        "registrosVencidos": registrosVencidos,
        "mostrarVencidos": mostrarVencidos,
        "renovarVenta": renovarVenta,
        "cancelarVenta": cancelarVenta
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
    dia = 0  # int
    mes = 0  # int
    ano = 0  # int
    fecha_vencimiento = []  # arreglo uni str
    diasDif = 0  # int
    estado = ""  # str
    if len(ventas) > 0:
        dia = validar["validarDia"](input("Ingrese el dia actual: "))
        mes = validar["validarMes"](input("Ingrese el mes actual: "))
        ano = validar["validarAno"](input("Ingrese el año actual: "))
        print("\n-LISTA DE VENTAS")
        print("----------------------------------------------------------------")
        print(
            "{0:10} {1:25} {2:12} {3:15}".format(
                "Tipo", "Descripción", "Precio", "Estado"
            )
        )
        for linea in ventas:
            if linea[0] == "Boleto":
                fecha_vencimiento = linea[1].split("-")[3:6]
            else:
                fecha_vencimiento = linea[1].split("-")[8:11]
            diasDif = ventaVencido(
                dia,
                mes,
                ano,
                int(fecha_vencimiento[0]),
                int(fecha_vencimiento[1]),
                int(fecha_vencimiento[2]),
            )
            if diasDif >= 7 and (
                linea[3] == "No Vendido\n" or linea[3] == "No Vendido"
            ):
                estado = "Vencida\n"
            else:
                estado = linea[3]
            if linea[0] == "Boleto":
                print(
                    "{0:10} {1:25} {2:10.2f} $ {3:8}".format(
                        linea[0],
                        "-".join(linea[1].split("-")[0:3]),
                        float(linea[2]),
                        estado,
                    ),
                    end="",
                )
            elif linea[0] == "Nomina":
                print(
                    "{0:10} {1:25} {2:10.2f} $ {3:8}".format(
                        linea[0],
                        "-".join(linea[1].split("-")[0:2]),
                        float(linea[2]),
                        estado.strip(),
                    ),
                )
        print("----------------------------------------------------------------")


def registrosNoVendidos(ventas, noVendidos):  # void
    if len(ventas) > 0 and len(noVendidos) == 0:
        for i in range(len(ventas)):
            if ventas[i][3].strip() == "No Vendido":
                noVendidos.append(ventas[i])


def mostrarNoVendidos(noVendidos):  # int
    n = 0  # int
    if len(noVendidos) > 0:
        print("\n-REGISTROS SIN VENDER")
        for i in range(len(noVendidos)):
            n += 1
            if noVendidos[i][0] == "Boleto":
                print(
                    "{0}. {1} - {2} - {3:.2f} $".format(
                        n,
                        noVendidos[i][0],
                        "-".join(noVendidos[i][1].split("-")[0:3]),
                        float(noVendidos[i][2]),
                    )
                )
            elif noVendidos[i][0] == "Nomina":
                print(
                    "{0}. {1} - {2} - {3:.2f} $".format(
                        n,
                        noVendidos[i][0],
                        "-".join(noVendidos[i][1].split("-")[0:2]),
                        float(noVendidos[i][2]),
                    )
                )
    return n


def vender(noVendidos, ventas):  # void
    reg = 0  # int
    n = 0  # int
    monto = 0.0  # float
    abono = 0.0  # float
    dia = 0  # int
    mes = 0  # int
    ano = 0  # int
    difFecha = 0  # int
    fecha = []  # arreglo uni string
    if len(noVendidos) > 0 and len(ventas) > 0:
        n = mostrarNoVendidos(noVendidos)
        reg = validar["validarInt"](input("Ingrese el registro (1-" + str(n) + "): "))
        while reg < 1 or reg > n:
            print("ERROR: Selección fuera de rango!")
            reg = validar["validarInt"](
                input("Ingrese el registro (1-" + str(n) + "): ")
            )
        monto = float(noVendidos[reg - 1][2])
        nombre = noVendidos[reg - 1][1]
        tipo = noVendidos[reg - 1][0]
        dia = validar["validarDia"](input("Ingrese el dia: "))
        mes = validar["validarMes"](input("Ingrese el mes: "))
        ano = validar["validarAno"](input("Ingrese el año: "))
        if tipo == "Boleto":
            difFecha = ventaVencido(
                dia,
                mes,
                ano,
                int(nombre.split("-")[3]),
                int(nombre.split("-")[4]),
                int(nombre.split("-")[5]),
            )
        else:
            difFecha = ventaVencido(
                dia,
                mes,
                ano,
                int(nombre.split("-")[8]),
                int(nombre.split("-")[9]),
                int(nombre.split("-")[10]),
            )
        if difFecha >= 7:
            print(
                "AVISO: El registro que desea pagar está vencido! Por favor renueve el pago"
            )
        else:
            abono = validar["validarFloat"](input("Ingrese el abono: "))
            archivo = validar["escribirArchivo"]("ventas.bin")
            comprobarAbono(abono, monto, ventas, nombre, tipo, archivo)


def restarPrecio(ventas, restante, nombreRegistro, archivo):  # void
    if archivo != None and len(ventas) > 0:
        for i in range(len(ventas)):
            if ventas[i][1] == nombreRegistro:
                archivo.write(
                    "{0}#{1}#{2}#No Vendido\n".format(
                        ventas[i][0], nombreRegistro, restante
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


def marcarVendido(ventas, nombreRegistro, archivo):  # void
    if archivo != None and len(ventas) > 0:
        for i in range(len(ventas)):
            if ventas[i][1] == nombreRegistro:
                archivo.write(
                    "{0}#{1}#{2}#Vendido\n".format(
                        ventas[i][0], nombreRegistro, 0
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


def eliminarRegistroAsiento(nombre):  # void
    archivo = object
    cantidad = []  # arreglo uni int
    ventas = []  # arreglo uni str
    archivo = validar["leerArchivo"]("ventas.bin")
    if archivo == None:
        return
    cantidad = solucion["cantidadReg"](archivo)
    ventas = solucion["iniMatriz"](cantidad)
    solucion["obtenerRegistros"](archivo, ventas)
    archivo = validar["escribirArchivo"]("ventas.bin")
    for i in range(len(ventas)):
        if ventas[i][1] != nombre:
            archivo.write(
                "{0}#{1}#{2}#{3}".format(
                    ventas[i][0], ventas[i][1], ventas[i][2], ventas[i][3]
                ).encode("utf-8")
            )
    print("--- VENTAS CANCELADAS ---")


def eliminarRegistroAvion(avion):  # void
    archivo = object
    cantidad = []  # arreglo uni int
    ventas = []  # arreglo uni str
    archivo = validar["leerArchivo"]("ventas.bin")
    if archivo == None:
        return
    cantidad = solucion["cantidadReg"](archivo)
    ventas = solucion["iniMatriz"](cantidad)
    solucion["obtenerRegistros"](archivo, ventas)
    archivo = validar["escribirArchivo"]("ventas.bin")
    for i in range(len(ventas)):
        if ventas[i][1].split("-")[0] != avion:
            archivo.write(
                "{0}#{1}#{2}#{3}".format(
                    ventas[i][0], ventas[i][1], ventas[i][2], ventas[i][3]
                ).encode("utf-8")
            )
    print("--- VENTAS CANCELADAS ---")


def ventaVencido(dia, mes, ano, diaV, mesV, anoV):  # int
    diasTotales = 0  # int
    diasVTotales = 0  # int
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diasTotales = 365 * (ano - 1) + ano // 4 - ano // 100 + ano // 400
    for i in range(1, mes):
        diasTotales += dias_mes[i - 1]
    diasTotales += dia - 1

    diasVTotales = 365 * (anoV - 1) + anoV // 4 - anoV // 100 + anoV // 400
    for i in range(1, mesV):
        diasVTotales += dias_mes[i - 1]
    diasVTotales += diaV - 1
    return diasTotales - diasVTotales


def comprobarAbono(abono, monto, ventas, nombreRegistro, tipo, archivo):  # void
    restante = 0.0  # float
    if abono < monto:
        restante = monto - abono
        restarPrecio(ventas, restante, nombreRegistro, archivo)
        print("--- ABONO REALIZADO ---")
        print("Falta: " + str(restante) + " $")
    elif abono > monto:
        restante = abono - monto
        marcarVendido(ventas, nombreRegistro, archivo)
        print("--- ABONO REALIZADO ---")
        if tipo == "Boleto":
            solucion_inv["boletoVendido"](
                nombreRegistro.split("-")[0],
                nombreRegistro.split("-")[1],
                nombreRegistro.split("-")[2],
            )
            print("--- BOLETO VENDIDO ---")
        elif tipo == "Nomina":
            print("--- NOMINA CREADA ---")
            solucion_rh["crearNomina"](nombreRegistro.split("-"))
        print("Devolución al usuario: " + str(restante) + " $")
    else:
        marcarVendido(ventas, nombreRegistro, archivo)
        print("--- ABONO REALIZADO ---")
        if tipo == "Boleto":
            solucion_inv["boletoVendido"](
                nombreRegistro.split("-")[0],
                nombreRegistro.split("-")[1],
                nombreRegistro.split("-")[2],
            )
            print("--- BOLETO VENDIDO ---")
        elif tipo == "Nomina":
            print("--- NOMINA CREADA ---")
            solucion_rh["crearNomina"](nombreRegistro.split("-"))


def registrosVencidos(ventas, vencidas):  # arreglo uni int
    dia = 0  # int
    mes = 0  # int
    ano = 0  # int
    diasDif = 0  # int
    fecha_vencido = []  # arreglo uni str
    if len(ventas) > 0 and len(vencidas) == 0:
        dia = validar["validarDia"](input("Ingrese el dia actual: "))
        mes = validar["validarMes"](input("Ingrese el mes actual: "))
        ano = validar["validarAno"](input("Ingrese el año actual: "))
        print("\n-PAGOS VENCIDOS")
        for i in range(len(ventas)):
            if ventas[i][0] == "Boleto":
                fecha_vencido = ventas[i][1].split("-")[3:6]
            else:
                fecha_vencido = ventas[i][1].split("-")[8:11]
            diasDif = ventaVencido(
                dia,
                mes,
                ano,
                int(fecha_vencido[0]),
                int(fecha_vencido[1]),
                int(fecha_vencido[2]),
            )
            if diasDif >= 7 and (
                ventas[i][3] == "No Vendido\n" or ventas[i][3] == "No Vendido"
            ):
                vencidas.append(ventas[i])
    return [int(dia), int(mes), int(ano)]


def mostrarVencidos(vencidas, fecha_actual):  # void
    n = 0  # int
    diasDif = 0  # int
    fecha_vencido = []  # arreglo uni str
    if len(vencidas) > 0:
        for i in range(len(vencidas)):
            n += 1
            if vencidas[i][0] == "Boleto":
                fecha_vencido = vencidas[i][1].split("-")[3:6]
            else:
                fecha_vencido = vencidas[i][1].split("-")[8:11]
            diasDif = ventaVencido(
                fecha_actual[0],
                fecha_actual[1],
                fecha_actual[2],
                int(fecha_vencido[0]),
                int(fecha_vencido[1]),
                int(fecha_vencido[2]),
            )
            if vencidas[i][0] == "Boleto":
                print(
                    "{0}. {1} - {2} - {3:.2f} $ - Vencido hace {4} días".format(
                        n,
                        vencidas[i][0],
                        "-".join(vencidas[i][1].split("-")[0:3]),
                        float(vencidas[i][2]),
                        diasDif,
                    )
                )
            else:
                print(
                    "{0}. {1} - {2} - {3:.2f} $ - Vencido hace {4} días".format(
                        n,
                        vencidas[i][0],
                        "-".join(vencidas[i][1].split("-")[0:2]),
                        float(vencidas[i][2]),
                        diasDif,
                    )
                )
    else:
        print("-----------------------------")
        print("No hay registros vencidos...")
        print("-----------------------------")


def renovarVenta(ventas, vencidas, fecha_actual, archivo):  # void
    n = 0  # int
    reg = []  # arreglo uni str
    aux = []  # arreglo uni str
    if len(vencidas) > 0 and archivo != None:
        n = validar["validarInt"](
            input("Ingrese su opción (1-" + str(len(vencidas)) + "): ")
        )
        for i in range(len(ventas)):
            reg = ventas[i]
            if ventas[i][1] == vencidas[n - 1][1]:
                aux = reg[1].split("-")
                if ventas[i][0] == "Boleto":
                    aux[3] = str(fecha_actual[0])
                    aux[4] = str(fecha_actual[1])
                    aux[5] = str(fecha_actual[2])
                else:
                    aux[8] = str(fecha_actual[0])
                    aux[9] = str(fecha_actual[1])
                    aux[10] = str(fecha_actual[2])
                reg[1] = "-".join(aux)
            archivo.write("#".join(reg).encode("utf-8"))
        print("--- VENTA RENOVADA ---")


def cancelarVenta(ventas, noVendidos, archivo):  # void
    n = 0  # int
    if len(noVendidos) > 0 and archivo != None:
        mostrarNoVendidos(noVendidos)
        n = validar["validarInt"](
            input("Ingrese su opción (1-" + str(len(noVendidos)) + "): ")
        )
        for i in range(len(ventas)):
            if ventas[i][1] != noVendidos[n - 1][1]:
                archivo.write("#".join(ventas[i]).encode("utf-8"))
        print("--- VENTA CANCELADA ---")


solucion = diccionario()
