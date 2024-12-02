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
        "calculosBasicos": calculosBasicos,
        "calculoIndemnizaciones": calculoIndemnizaciones,
        "generarArchivoLiq": generarArchivo,
        "eliminarRegistro": eliminarRegistro,
        "crearNomina": crearNomina,
        "razonCancelacion": razonCancelacion,
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
        nombre = validar["manejoNombre"](input("Ingrese el nombre del empleado: ")).title()
        apellido = validar["manejoNombre"](input("Ingrese el apellido del empleado: ")).title()
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
                "{0}#{1}#{2}#{3}#{4}#{5}#{6}#{7}#{8}#{9}\n".format(
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
    archivo = validar["leerArchivo"]("recursos_humanos/personal.bin")

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
    dias_no_trabajados = 0  # int
    motivo = ""  # str
    motivos = {1: "Renuncia", 2: "Despido"}

    nombre = validar["manejoNombre"](input("Ingrese el nombre del empleado: ")).title()
    apellido = validar["manejoNombre"](input("Ingrese el apellido del empleado: ")).title()
    posicion = buscar(archivo, nombre, apellido)
    if posicion == None:
        return

    print("\n\tMotivos de Liquidación\t\n1) Renuncia\n2) Despido\n3) Salir ")
    opcion = validar["validarOpcionDict"](input("Ingrese una opción: "), motivos)
    if opcion == len(motivos) + 1:
        return
    motivo = motivos[opcion]

    fila_columna = determinarTamaño(archivo)
    datos = iniTextoBinario(fila_columna[1])
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
    dias_no_trabajados = 30 - fecha_actual[0]
    archivo.close()

    calculos_basicos = calculosBasicos(
        dias_antiguedad, dias_no_trabajados, fecha_actual[1], sueldo_basico)
    indemnizaciones = calculoIndemnizaciones(
        dias_antiguedad, dias_no_trabajados, fecha_actual[1], sueldo_basico, motivo
    )
    registrarPago(
        datos, calculos_basicos, indemnizaciones, fecha_actual, dias_antiguedad, motivo, "pagos/pagos.bin"
    )
    print("¡Liquidación registrada en el módulo de pagos!")
    print("AVISO: Tiene un plazo máximo de 7 días para pagar la liquidación")
    print("Si se sobrepasa esta fecha el registro se eliminará")
    return



def calculosBasicos(dias_antiguedad, dias_no_trabajados, mes, sueldo_basico):  # tupla
    if (
        dias_antiguedad >= 0
        and dias_no_trabajados >= 0
        and mes >= 0
        and sueldo_basico >= 0
    ):

        dias_ano_actual = 0  # int
        dias_semestre = 0  # int
        comision_antiguedad = 0.0  # float
        aguinaldo = 0.0  # float
        sueldo_bruto = 0.0  # float
        jubilacion = 0.0  # float
        obra_social_pami = 0.0  # float
        sueldo_neto = 0.0  # float
        dias_ano_actual = mes * 30

        comision_antiguedad = (sueldo_basico * 0.01) * (dias_antiguedad / 365)
        if dias_ano_actual >= 180:
            dias_semestre = dias_ano_actual - 180
        aguinaldo = (dias_semestre / 180) * (sueldo_basico / 2)

        sueldo_bruto = sueldo_basico + aguinaldo + comision_antiguedad

        jubilacion = sueldo_bruto * 0.11
        obra_social_pami = sueldo_bruto * 0.03
        obra_social = sueldo_bruto * 0.03

        sueldo_neto = sueldo_bruto - jubilacion - obra_social_pami - obra_social
        
        remuneraciones = {
            "Sueldo Basico": sueldo_basico,
            "Antiguedad": comision_antiguedad,
            "Aguinaldo": aguinaldo
        }
        aportes = {
            "Jubilacion y/o Pension (SIPA)": jubilacion,
            "Obra Social Pami": obra_social_pami,
            "Obra Social Actual": obra_social
        }
        sueldos = {
            "Sueldo Basico": sueldo_basico,
            "Sueldo Bruto": sueldo_bruto,
            "Sueldo Neto": sueldo_neto,
        }
        return (remuneraciones, aportes, sueldos)


def calculoIndemnizaciones(
    dias_antiguedad, dias_no_trabajados, mes, sueldo_basico, motivo
    ): # Diccionario
    if (
        dias_antiguedad >= 0
        and dias_no_trabajados >= 0
        and mes >= 0
        and sueldo_basico >= 0
        and ((motivo == "Liq. Despido" or motivo == "Liq. Renuncia") 
             or motivo == "Despido" or motivo == "Renuncia")
    ):
        dias_ano_actual = 0 # int
        dias_vacaciones = 0 # int
        dias_ano_actual = mes * 30
        dias_vacaciones = vacaciones(dias_antiguedad / 365)
        
        vacaciones_no_gozadas = ((sueldo_basico / 25) * dias_vacaciones * (dias_ano_actual / 360))
        integracion_mes = (sueldo_basico / 30) * dias_no_trabajados
        integracion_sac = integracion_mes * 0.08333
        indemnizacion_despido = sueldo_basico * (dias_antiguedad / 365)
        
        dict_renuncia = {"Vacaciones no gozadas": vacaciones_no_gozadas}
        dict_despido = {
            "Vacaciones no gozadas": vacaciones_no_gozadas,
            "Integracion mes de despido": integracion_mes,
            "Sac de la integracion": integracion_sac,
            "Indemnizacion por despido": indemnizacion_despido
        }
        if motivo == "Renuncia" or motivo == "Despido": 
          tipos_indemnizaciones = {
            "Renuncia": dict_renuncia,
            "Despido": dict_despido
        }  
        else:
            tipos_indemnizaciones = {
                "Liq. Renuncia": dict_renuncia,
                "Liq. Despido": dict_despido
            }

        return tipos_indemnizaciones[motivo]


def generarArchivo(
    datos, fecha_actual, dias_antiguedad, calculos_basicos, indemnizaciones
    ): # void procedimiento
    if (
        len(datos) > 0
        and len(fecha_actual) > 0
        and dias_antiguedad >= 0
        and len(calculos_basicos) > 0
        and len(indemnizaciones) > 0
    ):
        total = 0.0 # float
        total += calculos_basicos[2]["Sueldo Neto"]
        archivo_nuevo = validar["crearArchivo"]("{} {} {}-{}-{}".format(
            datos[0], datos[1], fecha_actual[0], fecha_actual[1], fecha_actual[2]))
        encabezado ="""
                    Liquidacion Prestaciones Sociales
                            Fecha: {3}/{4}/{5}
----------------------------------------------------------------------
Nombre: {0} {1}                                Dni: {2} 
Fecha de Ingreso: {6}/{7}/{8}                  Antiguedad: {9:.1f} 
Fecha de Retiro: {3}/{4}/{5}                   
Sueldo Basico: {10:.2f}
----------------------------------------------------------------------
                            Remuneraciones
                            
    Detalle                                 Total $(ARS)\n""".format(
    datos[0], datos[1], int(datos[2]), fecha_actual[0], fecha_actual[1],
    fecha_actual[2], int(datos[7]), int(datos[8]), int(datos[9]),
    (dias_antiguedad/365), float(datos[6])
)
        archivo_nuevo.write(encabezado)
        for clave in calculos_basicos[0]:
            archivo_nuevo.write("{:<35} {:>20.2f}\n".format(
                clave, calculos_basicos[0][clave]))
            
        archivo_nuevo.write("{}\n{:<35} {:>20.2f}\n".format(
            ("-" * 70), "Sueldo Bruto", calculos_basicos[2]["Sueldo Bruto"]))
        
        archivo_nuevo.write("{}\n{:>47}\n".format(
            ("-" * 70), "Aportes del trabajador"))
        for clave in calculos_basicos[1]:
            archivo_nuevo.write("{:<35} {:>20.2f}\n".format(
                clave, calculos_basicos[1][clave]))
            
        archivo_nuevo.write("{}\n{:<35} {:>20.2f}\n".format(
            ("-" * 70), "Sueldo Neto", calculos_basicos[2]["Sueldo Neto"]))
        
        archivo_nuevo.write("{}\n{:>42}\n".format(
            ("-" * 70), "Indemnizaciones"))
        for clave in indemnizaciones:
            archivo_nuevo.write("{:<35} {:>20.2f}\n".format(
                clave, indemnizaciones[clave]))
            total += indemnizaciones[clave]
            
        archivo_nuevo.write("{}\n{:<35} {:>20.2f}\n".format(
            ("-" * 70), "Importe final a cobrar", total))
        
        archivo_nuevo.write("\n\n\n{0:<43} {0}\n".format("_" * 35))
        archivo_nuevo.write("Entregado por: Aerolineas Argentina\t\t\tRecibido por: {} {}".format(
            datos[0], datos[1]))


def registrarPago(
    datos, calculos_basicos, indemnizaciones, fecha_actual, dias_antiguedad, motivo, ruta):  # void
    archivo = object  # objeto
    totalPago = 0.0  # float
    archivo = validar["agregarArchivo"](ruta)

    if archivo == None:
        print("Object file -- does not exist")
        return
    totalPago = calculos_basicos[2]["Sueldo Neto"]
    for clave in indemnizaciones:
        totalPago += indemnizaciones[clave]
    for clave in calculos_basicos[1]:
        totalPago += calculos_basicos[1][clave]
        
    if motivo == "Despido":
        archivo.write("Liq. Despido#".encode("utf-8"))
    else:
        archivo.write("Liq. Renuncia#".encode("utf-8"))
    for i in range(len(datos)):
        archivo.write("{}-".format(datos[i].strip()).encode("utf-8"))
    for i in range(len(fecha_actual)):
        archivo.write("{}-".format(fecha_actual[i]).encode("utf-8"))
    archivo.write("{}-".format(dias_antiguedad / 365).encode("utf-8"))
    archivo.write("#{:.2f}#No Pagado\n".format(totalPago).encode("utf-8"))
    archivo.close()


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


def datosEmpleado(archivo, posicion, arreglo):  # arreglo uni str
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

        archivo = validar["leerArchivo"]("recursos_humanos/personal.bin")

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
    dia = 0  # int
    mes = 0  # int
    ano = 0  # int
    ventas_archivo = object
    if archivo != None and len(empleados) > 0:
        nombre = validar["manejoNombre"](input("Ingrese el nombre del empleado: "))
        apellido = validar["manejoNombre"](input("Ingrese el apellido del empleado: "))
        posicion = buscar(archivo, nombre, apellido)
        if posicion == None:
            return
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
        ventas_archivo = validar["agregarArchivo"]("ventas/ventas.bin")
        dia = validar["validarDia"](input("Ingrese el dia actual: "))
        mes = validar["validarMes"](input("Ingrese el mes actual: "))
        ano = validar["validarAno"](input("Ingrese el año actual: "))
        ventas_archivo.write(
            "Nomina#{0}-{1}-{2}-{3}-{4}-{5}-{6}-{7}-{8}-{9}-{10}#{11}#No Vendido".format(
                nombre,
                apellido,
                salario,
                salario_neto,
                ap_jub,
                ap_os,
                ap_sd,
                imp_gan,
                dia,
                mes,
                ano,
                deducciones,
            ).encode(
                "utf-8"
            )
        )
        print("--- REGISTRO DE NÓMINA CREADO EN EL MÓDULO DE VENTAS ---")


def crearNomina(datos):  # void
    nomina_archivo = object
    nomina_archivo = validar["crearArchivo"](
        "Nomina-{0}-{1}".format(datos[0], datos[1])
    )
    if nomina_archivo != None:
        nomina_archivo.write(
            "---------------------------------------------------------------\n"
        )
        nomina_archivo.write("                            Nomina                   \n")
        nomina_archivo.write(
            "---------------------------------------------------------------\n"
        )
        nomina_archivo.write(
            "Nombre: {0}                                 \n".format(datos[0])
        )
        nomina_archivo.write(
            "Apellido: {0}                               \n".format(datos[1])
        )
        nomina_archivo.write("                          Deducciones                 \n")
        nomina_archivo.write(
            "---------------------------------------------------------------\n"
        )
        nomina_archivo.write(
            "Aportes Jubilatorios: {0} %                 \n".format(datos[4])
        )
        nomina_archivo.write(
            "Aportes a la obra social: {0} %             \n".format(datos[5])
        )
        nomina_archivo.write(
            "Aportes sindicales: {0} %                   \n".format(datos[6])
        )
        nomina_archivo.write(
            "Impuesto a las ganancias: {0} $             \n".format(datos[7])
        )
        nomina_archivo.write(
            "---------------------------------------------------------------\n"
        )
        nomina_archivo.write(
            "Salario Base: {0} $         Salario Neto: {1} $ \n".format(
                datos[2], datos[3]
            )
        )
        nomina_archivo.write(
            "---------------------------------------------------------------\n"
        )
        nomina_archivo.close()


def razonCancelacion():  # string
    opcion = 0  # int
    print("\n-RAZONES DE CANCELACIÓN")
    print("1. Falla en el avión")
    print("2. Inconveniente con pasajero")
    opcion = validar["opcion"](input("Ingrese la opción (1-2): "))
    while opcion < 1 or opcion > 2:
        print("ERROR: Opción fuera de rango!")
        opcion = validar["opcion"](input("Ingrese la opción (1-2): "))
    if opcion == 1:
        return "Avion"
    else:
        return "Pasajero"


solucion = diccionario()
