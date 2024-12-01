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
        "registrosVencidos": registrosVencidos,
        "mostrarVencidos": mostrarVencidos,
        "renovarPago": renovarPago,
        "cancelarPago": cancelarPago,
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
    dia = 0  # int
    mes = 0  # int
    ano = 0  # int
    diasDif = 0  # int
    fecha_vencido = []  # arreglo uni str
    estado = ""  # str
    if len(pagos) > 0:
        dia = validar["validarDia"](input("Ingrese el dia actual: "))
        mes = validar["validarMes"](input("Ingrese el mes actual: "))
        ano = validar["validarAno"](input("Ingrese el año actual: "))
        print("\n-LISTA DE PAGOS")
        print("--------------------------------------------------")
        print(
            "{0:15} {1:15} {2:14} {3:8}".format(
                "Tipo", "Descripción", "Precio", "Estado"
            )
        )
        for linea in pagos:
            if linea[0] == "Artículo":
                fecha_vencido = linea[1].split("-")[2:5]
            else:
                fecha_vencido = linea[1].split("-")[10:13]
            diasDif = pagoVencido(
                dia,
                mes,
                ano,
                int(fecha_vencido[0]),
                int(fecha_vencido[1]),
                int(fecha_vencido[2]),
            )
            if diasDif >= 7 and linea[3] == "No Pagado\n":
                estado = "Vencido\n"
            else:
                estado = linea[3]
            if linea[0] == "Liq. Despido" or linea[0] == "Liq. Renuncia":
                print(
                    "{0:15} {1:15} {2:12.2f} $ {3:5}".format(
                        linea[0],
                        "-".join(linea[1].split("-")[0:2]),
                        float(linea[2]),
                        estado,
                    ),
                    end="",
                )
            else:
                print(
                    "{0:15} {1:15} {2:12.2f} $ {3:5}".format(
                        linea[0], linea[1].split("-")[0], float(linea[2]), estado
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
    nombre = ""  # string
    tipo = ""  # string
    dia = 0  # int
    mes = 0  # int
    ano = 0  # int
    difFecha = 0  # int
    fecha = []  # arreglo uni string
    archivo = object
    if len(noPagados) > 0 and len(pagos) > 0:
        print("\n-REGISTROS SIN PAGAR")
        n = mostrarNoPagados(noPagados)
        reg = validar["validarInt"](input("Ingrese el registro (1-" + str(n) + "): "))
        while reg < 1 or reg > n:
            print("ERROR: Selección fuera de rango!")
            reg = validar["validarInt"](
                input("Ingrese el registro (1-" + str(n) + "): ")
            )
        monto = float(noPagados[reg - 1][2])
        nombre = noPagados[reg - 1][1]
        tipo = noPagados[reg - 1][0]
        dia = validar["validarDia"](input("Ingrese el dia: "))
        mes = validar["validarMes"](input("Ingrese el mes: "))
        ano = validar["validarAno"](input("Ingrese el año: "))
        fecha = noPagados[reg - 1][1].split("-")[2:]
        if tipo == "Artículo":
            difFecha = pagoVencido(
                dia, mes, ano, int(fecha[0]), int(fecha[1]), int(fecha[2])
            )
        elif tipo == "Liq. Renuncia" or tipo == "Liq. Despido":
            difFecha = pagoVencido(
                dia,
                mes,
                ano,
                int(nombre.split("-")[10:13][0]),
                int(nombre.split("-")[10:13][1]),
                int(nombre.split("-")[10:13][2]),
            )
        if difFecha >= 7:
            print(
                "AVISO: El registro que desea pagar está vencido! Por favor renueve el pago"
            )
        else:
            abono = validar["validarFloat"](input("Ingrese el abono: "))
            archivo = validar["escribirArchivo"]("pagos.bin")
            comprobarAbono(abono, monto, pagos, nombre, archivo, tipo)
    else:
        print("-------------------------------------")
        print("Todos los registros están pagados...")
        print("-------------------------------------")


def comprobarAbono(abono, monto, pagos, nombreRegistro, archivo, tipo):  # void
    restante = 0  # float
    if abono < monto:
        restante = monto - abono
        restarPrecio(pagos, nombreRegistro, restante, archivo)
        print("--- ABONO REALIZADO ---")
        print("Falta: " + str(restante) + " $")
    elif abono > monto:
        restante = abono - monto
        marcarPagado(pagos, nombreRegistro, archivo)
        print("--- ABONO REALIZADO ---")
        if tipo == "Artículo":
            pagarArticulo(nombreRegistro)
        elif tipo == "Liq. Despido" or tipo == "Liq. Renuncia":
            pagarLiquidacion(nombreRegistro, tipo == "Liq. Despido")
        print("Devolución al usuario: " + str(restante) + " $")
    else:
        marcarPagado(pagos, nombreRegistro, archivo)
        print("--- ABONO REALIZADO ---")
        if tipo == "Artículo":
            pagarArticulo(nombreRegistro)
        elif tipo == "Liq. Despido" or tipo == "Liq. Renuncia":
            pagarLiquidacion(nombreRegistro, tipo == "Liq. Despido")


def mostrarNoPagados(noPagados):  # int
    n = 0  # int
    if len(noPagados) > 0:
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
    return n


def restarPrecio(pagos, nombreRegistro, restante, archivo):  # void
    if len(pagos) > 0 and archivo != None:
        for i in range(len(pagos)):
            if pagos[i][1] == nombreRegistro:
                archivo.write(
                    "{0}#{1}#{2}#No Pagado\n".format(
                        pagos[i][0], nombreRegistro, restante
                    ).encode("utf-8")
                )
            else:
                archivo.write(
                    "{0}#{1}#{2}#{3}\n".format(
                        pagos[i][0], pagos[i][1], pagos[i][2], pagos[i][3].strip()
                    ).encode("utf-8")
                )


def marcarPagado(pagos, nombreRegistro, archivo):  # void
    if len(pagos) > 0 and archivo != None:
        for i in range(len(pagos)):
            if pagos[i][1] == nombreRegistro:
                archivo.write(
                    "{0}#{1}#{2}#Pagado\n".format(
                        pagos[i][0], nombreRegistro, 0
                    ).encode("utf-8")
                )
            else:
                archivo.write(
                    "{0}#{1}#{2}#{3}\n".format(
                        pagos[i][0], pagos[i][1], pagos[i][2], pagos[i][3].strip()
                    ).encode("utf-8")
                )


def pagoVencido(dia, mes, ano, diaV, mesV, anoV):  # int
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


def pagarArticulo(nombreRegistro):  # void
    articulo = ""  # str
    cantidad = 0  # int
    articulo = nombreRegistro.split("-")[0]
    cantidad = int(nombreRegistro.split("-")[1])
    solucion_inv["agregar"](articulo, cantidad)
    print("--- ARTÍCULO PAGADO Y AGREGADO AL INVENTARIO ---")


def pagarLiquidacion(nombreRegistro, esDespido):  # void
    datos = []  # arreglo uni str
    fecha_actual = []  # arreglo uni str
    dias_antiguedad = ""  # str
    calculos = []  # arreglo uni float

    datos = nombreRegistro.split("-")[0:10]
    fecha_actual = nombreRegistro.split("-")[10:13]
    dias_antiguedad = nombreRegistro.split("-")[13]
    if esDespido:
        calculos = nombreRegistro.split("-")[14:27]
    else:
        calculos = nombreRegistro.split("-")[14:30]
    solucion_rh["generarArchivoDespido"](
        datos, calculos, fecha_actual, float(dias_antiguedad)
    )
    solucion_rh["eliminarRegistro"](
        nombreRegistro.split("-")[0], nombreRegistro.split("-")[1]
    )
    print("--- LIQUIDACIÓN CREADA ---")


def eliminarRegistro(nombreRegistro, pagos):  # void
    archivo = object
    archivo = validar["escribirArchivo"]("pagos.bin")
    if archivo != None:
        for i in range(len(pagos)):
            if pagos[i][1] != nombreRegistro:
                archivo.write("#".join(pagos[i]).encode("utf-8"))
        archivo.close()
    print("--- REGISTRO DE PAGO ELIMINADO ---")


def registrosVencidos(pagos, vencidos):  # arreglo uni int
    dia = 0  # int
    mes = 0  # int
    ano = 0  # int
    diasDif = 0  # int
    fecha_vencido = []  # arreglo uni str
    if len(pagos) > 0 and len(vencidos) == 0:
        dia = validar["validarDia"](input("Ingrese el dia actual: "))
        mes = validar["validarMes"](input("Ingrese el mes actual: "))
        ano = validar["validarAno"](input("Ingrese el año actual: "))
        print("\n-PAGOS VENCIDOS")
        for i in range(len(pagos)):
            if pagos[i][0] == "Artículo":
                fecha_vencido = pagos[i][1].split("-")[2:5]
            else:
                fecha_vencido = pagos[i][1].split("-")[10:13]
            diasDif = pagoVencido(
                dia,
                mes,
                ano,
                int(fecha_vencido[0]),
                int(fecha_vencido[1]),
                int(fecha_vencido[2]),
            )
            if diasDif >= 7 and pagos[i][3] == "No Pagado\n":
                vencidos.append(pagos[i])
    return [int(dia), int(mes), int(ano)]


def mostrarVencidos(vencidos, fecha_actual):  # void
    n = 0  # int
    diasDif = 0  # int
    fecha_vencido = []  # arreglo uni str
    if len(vencidos) > 0:
        for i in range(len(vencidos)):
            n += 1
            if vencidos[i][0] == "Artículo":
                fecha_vencido = vencidos[i][1].split("-")[2:5]
            else:
                fecha_vencido = vencidos[i][1].split("-")[10:13]
            diasDif = pagoVencido(
                fecha_actual[0],
                fecha_actual[1],
                fecha_actual[2],
                int(fecha_vencido[0]),
                int(fecha_vencido[1]),
                int(fecha_vencido[2]),
            )
            print(
                "{0}. {1} - {2} - {3:.2f} $ - Vencido hace {4} días".format(
                    n,
                    vencidos[i][0],
                    "-".join(vencidos[i][1].split("-")[0:1]),
                    float(vencidos[i][2]),
                    diasDif,
                )
            )
    else:
        print("-----------------------------")
        print("No hay registros vencidos...")
        print("-----------------------------")


def renovarPago(pagos, vencidos, fecha_actual, archivo):  # void
    n = 0  # int
    reg = []  # arreglo uni str
    aux = []  # arreglo uni str
    if len(vencidos) > 0 and archivo != None:
        n = validar["validarInt"](
            input("Ingrese su opción (1-" + str(len(vencidos)) + "): ")
        )
        for i in range(len(pagos)):
            reg = pagos[i]
            if pagos[i][1] == vencidos[n - 1][1]:
                aux = reg[1].split("-")
                if pagos[i][0] == "Artículo":
                    aux[2] = str(fecha_actual[0])
                    aux[3] = str(fecha_actual[1])
                    aux[4] = str(fecha_actual[2])
                else:
                    aux[10] = str(fecha_actual[0])
                    aux[11] = str(fecha_actual[1])
                    aux[12] = str(fecha_actual[2])
                reg[1] = "-".join(aux)
            archivo.write("#".join(reg).encode("utf-8"))
        print("--- PAGO RENOVADO ---")


def cancelarPago(pagos, noPagados, archivo):  # void
    n = 0  # int
    if len(noPagados) > 0 and archivo != None:
        mostrarNoPagados(noPagados)
        n = validar["validarInt"](
            input("Ingrese su opción (1-" + str(len(noPagados)) + "): ")
        )
        for i in range(len(pagos)):
            if pagos[i][1] != noPagados[n - 1][1]:
                archivo.write("#".join(pagos[i]).encode("utf-8"))
        print("--- PAGO CANCELADO ---")


solucion = diccionario()
