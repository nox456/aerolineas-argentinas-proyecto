from .utilitarias_rh import validar


def diccionario():
    return {
        "listar": listar,
        "agregar": agregar,
        "liquidacion": liquidacion,
        "cantidadReg": cantidadReg,
        "iniMatriz": iniMatriz,
        "obtenerRegistros": obtenerRegistros,
        "nomina": nomina,
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
        archivo.close()
    else:
        print("-------------------")
        print("No hay registros...")
        print("-------------------")


def listar(empleados):  # void

    if len(empleados) > 0:

        print(
            "----------------------------------------------------------------------------------------------------------------------"
        )
        print(
            "{0:10}  {1:10}  {2:8}  {3:2}  {4:17}  {5:25}  {6:10}    {7:15}".format(
                "Nombre",
                "Apellido",
                "Cédula",
                "Edad",
                "Año de Nacimiento",
                "Cargo",
                "Salario",
                "Fecha de Ingreso",
            )
        )
        for linea in empleados:
            print(
                "{0:10}  {1:10}  {2:7}  {3:<4}  {4:<17}  {5:25}  {6:<10}$    {7:<2} / {8:<2} / {9:<4}".format(
                    linea[0],
                    linea[1],
                    int(linea[2]),
                    int(linea[3]),
                    int(linea[4]),
                    linea[5],
                    float(linea[6]),
                    int(linea[7]),
                    int(linea[8]),
                    int(linea[9]),
                )
            )
        print(
            "----------------------------------------------------------------------------------------------------------------------"
        )


def agregar(archivo, roles):  # void
    nombre = ""  # str
    apellido = ""  # str
    cedula = 0  # int
    edad = 0  # int
    fecha = 0  # int
    cargo = ""  # str
    salario = 0.0  # float
    nombre_rol = ""  # str
    salario_rol = 0.0  # float
    dia_i = 0  # int
    mes_i = 0  # int
    ano_i = 0  # int
    n = 0  # int
    indice_rol = 0  # int
    if archivo != None and len(roles) > 0:
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        cedula = validar["entero"](input("Ingrese la cédula del empleado: "))
        edad = validar["entero"](input("Ingrese la edad del empleado: "))
        fecha = validar["entero"](input("Ingrese el año de nacimiento del empleado: "))
        dia_i = validar["validarDia"](input("Ingrese el día de ingreso: "))
        mes_i = validar["validarMes"](input("Ingrese el mes de ingreso: "))
        ano_i = validar["validarAno"](input("Ingrese el año de ingreso: "))

        print("\n---- Lista de Roles/Cargos disponibles ----")
        for rol in roles:
            nombre_rol = rol[0]
            salario_rol = float(rol[1])
            n += 1
            print("{0:2}. {1} - {2:,} $".format(n, nombre_rol, salario_rol))

        indice_rol = validar["opcion"](
            input("\nIngrese el rol del empleado (1-" + str(n) + "): ")
        )
        if indice_rol > n:
            print("ERROR: Opción no válida")
        else:
            n = 0
            for rol in roles:
                n += 1
                if n == indice_rol:
                    cargo = rol[0]
                    salario = float(rol[1])
            archivo.write(
                "\n{0}#{1}#{2}#{3}#{4}#{5}#{6}#{7}#{8}#{9}".format(
                    nombre,
                    apellido,
                    cedula,
                    edad,
                    fecha,
                    cargo,
                    salario,
                    dia_i,
                    mes_i,
                    ano_i,
                ).encode("utf-8")
            )
            print("EMPLEADO REGISTRADO!")


def liquidacion():  # void
    archivo = object  # objeto
    archivo = validar["leerArchivo"]("personal.bin")

    if archivo == None:
        print("Object file -- does not exist")
        return

    opcion = 0  # int
    fila_columna = [0, 0]
    datos = []  # arreglo uni str
    nombre = ""  # str
    apellido = ""  # str
    fecha_ingreso = [0, 0, 0]  # arreglo uni int
    fecha_actual = [0, 0, 0]  # arreglo uni int
    sueldo_basico = 0.0  # float
    posicion = 0  # int
    dias_antiguedad = 0  # int
    dias_vacaciones = 0  # int
    dias_no_trabajados = 0  # int
    motivo = ""  # str
    motivos = {1: "Renuncia", 2: "Despido"}
    funciones = {"Renuncia": calculosRenuncia, "Despido": calculosDespido}
    archivos = {"Renuncia": generarArchivoRenuncia, "Despido": generarArchivoDespido}

    print("\n\tMotivos de Liquidación\t\n1) Renuncia\n2) Despido\n3) Salir ")
    opcion = validar["validarOpcionDict"](input("Ingrese una opción: "), funciones)
    if opcion == len(funciones) + 1:
        return
    motivo = motivos[opcion]

    nombre = validar["manejoNombre"](input("Ingrese el nombre del empleado: ")).title()
    apellido = validar["manejoNombre"](
        input("Ingrese el apellido del empleado: ")
    ).title()
    posicion = buscar(archivo, nombre, apellido)
    if posicion == None:
        return

    fila_columna = determinarTamaño(archivo)
    datos = iniTextoBinario(fila_columna[0])
    datos = datosEmpleado(archivo, posicion, datos)
    fecha_ingreso[0] = int(datos[7])
    fecha_ingreso[1] = int(datos[8])
    fecha_ingreso[2] = int(datos[9])
    fecha_actual[0] = validar["validarDia"](input("Ingrese el día actual: "))
    fecha_actual[1] = validar["validarMes"](input("Ingrese el mes actual: "))
    fecha_actual[2] = validar["validarAno"](input("Ingrese el año actual: "))
    sueldo_basico = float(datos[6])
    dias_antiguedad = (
        (fecha_actual[0] - fecha_ingreso[0])
        + (fecha_actual[1] - fecha_ingreso[1]) * 30
        + (fecha_actual[2] - fecha_ingreso[2]) * 365
    )
    dias_vacaciones = vacaciones((dias_antiguedad / 365))
    dias_no_trabajados = 30 - fecha_actual[0]
    archivo.close()

    calculos = funciones[motivo](
        dias_antiguedad,
        dias_vacaciones,
        dias_no_trabajados,
        fecha_actual[1],
        sueldo_basico,
    )
    archivos[motivo](datos, calculos, fecha_actual, dias_antiguedad)
    # registrarPago(nombre, apellido, calculos[-1], calculos[5:8], "pagos/pagos.bin")
    eliminarRegistro(nombre, apellido)
    print("¡Liquidación Exitosa!")
    return


def generarArchivoRenuncia(datos, calculos, fecha_actual, dias_antiguedad):  # void
    if (
        len(datos) > 0
        and len(calculos) > 0
        and len(fecha_actual) > 0
        and dias_antiguedad >= 0
    ):
        archivo_nuevo = validar["crearArchivo"](
            "Utilidades {} {}.{}-{}-{}".format(
                datos[0], datos[1], fecha_actual[0], fecha_actual[1], fecha_actual[2]
            )
        )
        archivo_nuevo.write(
            """
                    Liquidacion Prestaciones Sociales
                            Fecha: {3}/{4}/{5}
----------------------------------------------------------------------
Nombre: {0} {1}                            Dni: {2} 
Fecha de Ingreso: {6}/{7}/{8}                  Antiguedad: {9:.1f} 
Fecha de Retiro: {3}/{4}/{5}                   Motivo del retiro: Renuncia
Sueldo Basico: {10:.2f}
----------------------------------------------------------------------
                            Remuneraciones
                            
    Detalle                                 Total $(ARS)
Sueldo Basico                               {10:.2f}
Antiguedad                                  {11:.2f}
Aguinaldo                                   {12:.2f}
----------------------------------------------------------------------
Sueldo Bruto                                {13:.2f}
----------------------------------------------------------------------
                            Aportes del trabajador
                        
Jubilacion y/o Pension (SIPA)               {14:.2f}
Obra Social PAMI                            {15:.2f}
Obra Social Actual                          {16:.2f}
----------------------------------------------------------------------
Sueldo Neto                                 {17:.2f}
----------------------------------------------------------------------
                            Indemnizaciones
                            
Vacaciones no gozadas                       {18:.2f}
----------------------------------------------------------------------
Importe final a cobrar                      {19:.2f}

                
                
                
___________________________________        _______________________________
Entregado por: Aerolineas Argentina        Recibido por: {0} {1}
                                                                
                """.format(
                datos[0],
                datos[1],
                int(datos[2]),
                fecha_actual[0],
                fecha_actual[1],
                fecha_actual[2],
                int(datos[7]),
                int(datos[8]),
                int(datos[9]),
                (dias_antiguedad / 365),
                float(datos[6]),
                calculos[3],
                calculos[4],
                calculos[1],
                calculos[5],
                calculos[6],
                calculos[7],
                calculos[2],
                calculos[8],
                calculos[9],
            )
        )

        archivo_nuevo.close()
        return


def generarArchivoDespido(datos, calculos, fecha_actual, dias_antiguedad):
    if (
        len(datos) > 0
        and len(calculos) > 0
        and len(fecha_actual) > 0
        and dias_antiguedad >= 0
    ):
        archivo_nuevo = validar["crearArchivo"](
            "Utilidades {} {}.{}-{}-{}".format(
                datos[0], datos[1], fecha_actual[0], fecha_actual[1], fecha_actual[2]
            )
        )

        archivo_nuevo.write(
            """
                    Liquidacion Prestaciones Sociales
                            Fecha: {3}/{4}/{5}
----------------------------------------------------------------------
Nombre: {0} {1}                            Dni: {2} 
Fecha de Ingreso: {6}/{7}/{8}                  Antiguedad: {9:.1f} 
Fecha de Retiro: {3}/{4}/{5}                   Motivo del retiro: Despido
Sueldo Basico: {10:.2f}
----------------------------------------------------------------------
                            Remuneraciones
                            
    Detalle                                 Total $(ARS)
Sueldo Basico                               {10:.2f}
Antiguedad                                  {11:.2f}
Aguinaldo                                   {12:.2f}
----------------------------------------------------------------------
Sueldo Bruto                                {13:.2f}
----------------------------------------------------------------------
                            Aportes del trabajador
                        
Jubilacion y/o Pension (SIPA)               {14:.2f}
Obra Social PAMI                            {15:.2f}
Obra Social Actual                          {16:.2f}
----------------------------------------------------------------------
Sueldo Neto                                 {17:.2f}
----------------------------------------------------------------------
                            Indemnizaciones
                            
Vacaciones no gozadas                       {18:.2f}
Integracion mes de despido                  {19:.2f}
Sac de la integracion                       {20:.2f}
Indemnizacion por Despido                   {21:.2f}

----------------------------------------------------------------------
Importe final a cobrar                      {22:.2f}

                
                
                
___________________________________        _______________________________
Entregado por: Aerolineas Argentina        Recibido por: {0} {1}
                                                                
                """.format(
                datos[0],
                datos[1],
                int(datos[2]),
                fecha_actual[0],
                fecha_actual[1],
                fecha_actual[2],
                int(datos[7]),
                int(datos[8]),
                int(datos[9]),
                (dias_antiguedad / 365),
                float(datos[6]),
                calculos[3],
                calculos[4],
                calculos[1],
                calculos[5],
                calculos[6],
                calculos[7],
                calculos[2],
                calculos[8],
                calculos[9],
                calculos[10],
                calculos[11],
                calculos[12],
            )
        )

        archivo_nuevo.close()
        return


def calculosRenuncia(
    dias_antiguedad, dias_vacaciones, dias_no_trabajados, mes, sueldo_basico
):  # tupla
    if (
        dias_antiguedad >= 0
        and dias_vacaciones >= 0
        and dias_no_trabajados >= 0
        and mes >= 0
        and sueldo_basico >= 0
    ):

        dias_ano_actual = 0  # int
        dias_semestre = 0  # int
        comision_antiguedad = 0.0  # float
        vacaciones_no_gozadas = 0.0  # float
        aguinaldo = 0.0  # float
        sueldo_bruto = 0.0  # float
        jubilacion = 0.0  # float
        obra_social_pami = 0.0  # float
        sueldo_neto = 0.0  # float
        dias_ano_actual = mes * 30

        comision_antiguedad = (sueldo_basico * 0.01) * (dias_antiguedad / 365)
        vacaciones_no_gozadas = (
            (sueldo_basico / 25) * dias_vacaciones * (dias_ano_actual / 360)
        )
        if dias_ano_actual >= 180:
            dias_semestre = dias_ano_actual - 180
        aguinaldo = (dias_semestre / 180) * (sueldo_basico / 2)

        sueldo_bruto = sueldo_basico + aguinaldo + comision_antiguedad

        jubilacion = sueldo_bruto * 0.11
        obra_social_pami = sueldo_bruto * 0.03
        obra_social = sueldo_bruto * 0.03

        sueldo_neto = sueldo_bruto - jubilacion - obra_social_pami - obra_social
        total = sueldo_neto + vacaciones_no_gozadas

        calculos = (
            sueldo_basico,
            sueldo_bruto,
            sueldo_neto,
            comision_antiguedad,
            aguinaldo,
            jubilacion,
            obra_social_pami,
            obra_social,
            vacaciones_no_gozadas,
            total,
        )

        return calculos


def calculosDespido(
    dias_antiguedad, dias_vacaciones, dias_no_trabajados, mes, sueldo_basico
):  # tupla
    if (
        dias_antiguedad >= 0
        and dias_vacaciones >= 0
        and dias_no_trabajados >= 0
        and mes >= 0
        and sueldo_basico >= 0
    ):

        dias_ano_actual = 0  # int
        dias_semestre = 0  # int
        comision_antiguedad = 0.0  # float
        vacaciones_no_gozadas = 0.0  # float
        integracion_mes = 0.0  # float
        integracion_sac = 0.0  # float
        indemnizacion_despido = 0.0  # float
        aguinaldo = 0.0  # float
        sueldo_bruto = 0.0  # float
        jubilacion = 0.0  # float
        obra_social_pami = 0.0  # float
        sueldo_neto = 0.0  # float
        total = 0.0  # float
        dias_ano_actual = mes * 30

        comision_antiguedad = (sueldo_basico * 0.01) * (dias_antiguedad / 365)
        vacaciones_no_gozadas = (
            (sueldo_basico / 25) * dias_vacaciones * (dias_ano_actual / 360)
        )
        integracion_mes = (sueldo_basico / 30) * dias_no_trabajados
        integracion_sac = integracion_mes * 0.08333
        indemnizacion_despido = sueldo_basico * (dias_antiguedad / 365)
        if dias_ano_actual >= 180:
            dias_semestre = dias_ano_actual - 180
        aguinaldo = (dias_semestre / 180) * (sueldo_basico / 2)

        sueldo_bruto = sueldo_basico + comision_antiguedad + aguinaldo

        jubilacion = sueldo_bruto * 0.11
        obra_social_pami = sueldo_bruto * 0.03
        obra_social = sueldo_bruto * 0.03
        sueldo_neto = sueldo_bruto - jubilacion - obra_social_pami - obra_social
        total = (
            sueldo_neto
            + vacaciones_no_gozadas
            + integracion_mes
            + integracion_sac
            + indemnizacion_despido
        )

        calculos = (
            sueldo_basico,
            sueldo_bruto,
            sueldo_neto,
            comision_antiguedad,
            aguinaldo,
            jubilacion,
            obra_social_pami,
            obra_social,
            vacaciones_no_gozadas,
            integracion_mes,
            integracion_sac,
            indemnizacion_despido,
            total,
        )

        return calculos


def registrarPago(nombre, apellido, total, impuestos, ruta):  # void
    archivo = object  # objeto
    archivo = validar["agregarArchivo"](ruta)

    if archivo == None:
        print("Object file -- does not exist")
        return

    if (
        validar["validarNombre"](nombre)
        and validar["validarNombre"](apellido)
        and total >= 0
        and len(impuestos) > 0
    ):
        archivo.write(
            "Pago Liquidación de {} {}#{:.2f}\n".format(nombre, apellido, total).encode(
                "utf-8"
            )
        )
        archivo.write(
            "Aporte jubilatorio por liquidación#{:.3f}\n".format(impuestos[0]).encode(
                "utf-8"
            )
        )
        archivo.write(
            "Aporte Obra Social (PAMI) por liquidación#{:.3f}\n".format(
                impuestos[1]
            ).encode("utf-8")
        )
        archivo.write(
            "Aporte Obra Social por liquidación#{:.3f}\n".format(impuestos[2]).encode(
                "utf-8"
            )
        )
        archivo.close()
        return
    return


def vacaciones(años_antiguedad):  # int
    if años_antiguedad >= 0:
        if 0 <= años_antiguedad < 0.5:
            return 0
        if 0.5 <= años_antiguedad < 5:
            return 14
        elif 5 <= años_antiguedad < 10:
            return 21
        elif 10 <= años_antiguedad < 20:
            return 28
        else:
            return 35


def datosEmpleado(archivo, posicion, arreglo):  # void
    if archivo == None:
        print("Object file -- does not exist")
        return

    if posicion >= 0 and len(arreglo) > 0:
        indice = 0  # int
        for campo in archivo:
            if indice == posicion:
                arreglo = campo.decode("utf-8").split("#")
                archivo.seek(0)
                return arreglo
            indice += 1


def eliminarRegistro(nombre, apellido):  # void
    if validar["validarNombre"](nombre) and validar["validarNombre"](apellido):

        posicion = 0  # int
        fila_columna = [0, 0]  # arreglo uni int
        texto_binario = []  # arreglo bi str
        archivo = object  # objeto

        archivo = validar["leerArchivo"]("personal.bin")

        if archivo == None:
            print("Object file -- does not exist")
            return

        posicion = buscar(archivo, nombre, apellido)
        if posicion == None:
            return
        fila_columna = determinarTamaño(archivo)
        texto_binario = iniTextoBinario(fila_columna[0])
        valoresArregloBinario(texto_binario, archivo)
        archivo.close()

        archivo = validar["escribirArchivo"]("recursos_humanos/personal.bin")
        if archivo == None:
            print("Object file -- does not exist")
            return

        for i in range(len(texto_binario)):
            if i != posicion:
                archivo.write(texto_binario[i].encode("utf-8"))

        archivo.close()
        return


def buscar(archivo, nombre, apellido):  # int
    if archivo == None:
        print("Object file -- does not exist")
        return

    if validar["validarNombre"](nombre) and validar["validarNombre"](apellido):
        n = 0  # int
        band = True  # bool
        for i in archivo:
            fila = i.decode("utf-8").split("#")
            if (fila[0].lower()) == nombre.lower() and (
                fila[1].lower()
            ) == apellido.lower():
                band = False
                archivo.seek(0)
                return n
            n += 1
        if band:
            print(
                "El empleado {} {} no se encuentra registrado".format(nombre, apellido)
            )
            archivo.seek(0)
            return None


def generarLinea(arreglo):  # str
    if len(arreglo) > 0:
        linea = ""
        for i in range(len(arreglo)):
            if i != (len(arreglo) - 1):
                linea += "{}#".format(arreglo[i])
            else:
                linea += arreglo[i]
        return linea


def determinarTamaño(archivo):  # arreglo uni int
    if archivo == None:
        print("Object file -- does not exist")
        return [0, 0]

    fila = 0  # int
    columna = 0  # int
    bandera = True  # bool
    fila_columna = [0, 0]  # arreglo uni int
    campo = []  # arreglo uni str
    for i in archivo:
        fila += 1
        campo = i.decode("utf-8").split("#")
        if bandera:
            columna = len(campo)
            bandera = False
        elif columna < len(campo):
            columna = len(campo)
    fila_columna[0] = fila
    fila_columna[1] = columna
    archivo.seek(0)
    return fila_columna


def iniTextoBinario(filas):  # arreglo uni str
    if filas > 0:
        return ["e" for i in range(filas)]


def valoresArregloBinario(arreglo, archivo):  # void
    if archivo == None:
        print("Object file -- does not exist")
        return
    if len(arreglo) > 0:
        indice = 0  # int
        for i in archivo:
            fila = i.decode("utf-8").split("#")
            fila = generarLinea(fila)
            arreglo[indice] = fila
            indice += 1
        archivo.seek(0)
    return


def nomina(archivo, empleados):
    nombre = ""  # str
    apellido = ""  # str
    posicion = 0  # int
    ap_jub = 0.0  # float
    ap_os = 0.0  # float
    ap_sd = 0.0  # float
    imp_gan = 0.0  # float
    deducciones = 0.0  # float
    salario = 0.0  # float
    salario_neto = 0.0  # float
    nomina_archivo = object
    nombre = validar["manejoNombre"](input("Ingrese el nombre del empleado: "))
    apellido = validar["manejoNombre"](input("Ingrese el apellido del empleado: "))
    posicion = buscar(archivo, nombre, apellido)
    salario = float(empleados[posicion][6])
    print("\n--- Deducciones ---\n")
    ap_jub = validar["validarFloat"](input("Aportes Jubilatorios (%): "))
    ap_os = validar["validarFloat"](input("Aportes a la obra social (%): "))
    ap_sd = validar["validarFloat"](input("Aportes sindicales (%): "))
    imp_gan = validar["validarFloat"](input("Impuesto a las ganancias ($): "))
    deducciones = (
        (salario * ap_jub / 100)
        + (salario * ap_os / 100)
        + (salario * ap_sd / 100)
        + imp_gan
    )
    salario_neto = salario - deducciones
    nomina_archivo = validar["crearArchivo"]("Nomina-{0}-{1}".format(nombre, apellido))
    nomina_archivo.write("---------------------------------------------------------------\n")
    nomina_archivo.write("                            Nomina                   \n")
    nomina_archivo.write("---------------------------------------------------------------\n")
    nomina_archivo.write(
        "Nombre: {0}                                 \n".format(nombre)
    )
    nomina_archivo.write(
        "Apellido: {0}                               \n".format(apellido)
    )
    nomina_archivo.write("                          Deducciones                 \n")
    nomina_archivo.write("---------------------------------------------------------------\n")
    nomina_archivo.write(
        "Aportes Jubilatorios: {0} %                 \n".format(ap_jub)
    )
    nomina_archivo.write(
        "Aportes a la obra social: {0} %             \n".format(ap_os)
    )
    nomina_archivo.write(
        "Aportes sindicales: {0} %                   \n".format(ap_sd)
    )
    nomina_archivo.write(
        "Impuesto a las ganancias: {0} $             \n".format(imp_gan)
    )
    nomina_archivo.write("---------------------------------------------------------------\n")
    nomina_archivo.write(
        "Salario Base: {0} $         Salario Neto: {1} $ \n".format(
            salario, salario_neto
        )
    )
    nomina_archivo.write("---------------------------------------------------------------\n")
    nomina_archivo.close()
    print("¡Nómina Creada!")


solucion = diccionario()
