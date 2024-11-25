from .utilitarias_rh import validar


def diccionario():
    return {
        "listar": listar,
        "agregar": agregar,
    }


def listar(archivo):  # void

    if archivo != None:

        print(
            "--------------------------------------------------------------------------------------------------------------------------------------------------------------"
        )
        print(
            "{0:10}  {1:10}  {2:8}  {3:2}  {4:20}  {5:25}  {6:10}    {7:15}  {8:15}  {9:15}".format(
                "Nombre",
                "Apellido",
                "Cédula",
                "Edad",
                "Año de Nacimiento",
                "Cargo",
                "Salario",
                "Dia de ingreso",
                "Mes de ingreso",
                "Año de ingreso"
            )
        )
        for fila in archivo:
            campos = fila.split("#")
            print(
                "{0:10}  {1:10}  {2:7}  {3:<4}  {4:<20}  {5:25}  {6:<10}$    {7:<15}  {8:<15}  {9:<15}".format(
                    campos[0],
                    campos[1],
                    int(campos[2]),
                    int(campos[3]),
                    int(campos[4]),
                    campos[5],
                    float(campos[6]),
                    int(campos[7]),
                    int(campos[8]),
                    int(campos[9])
                )
            )
        print(
            "--------------------------------------------------------------------------------------------------------------------------------------------------------------"
        )


def agregar(archivoEmpleados, archivoRoles):  # void
    nombre = ""  # str
    apellido = ""  # str
    cedula = 0  # int
    edad = 0  # int
    fecha = 0  # int
    cargo = ""  # str
    salario = 0.0  # float
    nombre_rol = ""  # str
    salario_rol = 0.0  # float
    dia_i = 0 # int
    mes_i = 0 #int
    ano_i = 0 # int
    n = 0  # int
    indice_rol = 0  # int
    if archivoEmpleados != None and archivoRoles != None:
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        cedula = validar["entero"](input("Ingrese la cédula del empleado: "))
        edad = validar["entero"](input("Ingrese la edad del empleado: "))
        fecha = validar["entero"](input("Ingrese el año de nacimiento del empleado: "))
        dia_i = validar["validarDia"](input("Ingrese el día de ingreso: "))
        mes_i = validar["validarMes"](input("Ingrese el mes de ingreso: "))
        ano_i = validar["validarAno"](input("Ingrese el año de ingreso: "))
        
        print("---- Lista de Roles/Cargos disponibles ----")
        for rol in archivoRoles:
            nombre_rol = rol.split("#")[0]
            salario_rol = float(rol.split("#")[1])
            n += 1
            print("{0:2}. {1} - {2:,} $".format(n, nombre_rol, salario_rol))
            
        indice_rol = validar["opcion"](
            input("Ingrese el rol del empleado (1-" + str(n) + "): "))
        if indice_rol > n:
            print("ERROR: Opción no válida")
        else:
            n = 0
            archivoRoles.seek(0)
            for rol in archivoRoles:
                n += 1
                if n == indice_rol:
                    cargo = rol.decode("utf-8").split("#")[0]
                    salario = float(rol.decode("utf-8").split("#")[1])
            archivoEmpleados.write("\n{0}#{1}#{2}#{3}#{4}#{5}#{6}#{7}#{8}#{9}".format(nombre,
                                                                                    apellido,
                                                                                    cedula,
                                                                                    edad,
                                                                                    fecha,
                                                                                    cargo,
                                                                                    salario,
                                                                                    dia_i,
                                                                                    mes_i,
                                                                                    ano_i))
            print("EMPLEADO REGISTRADO!")







recursos_humanos = diccionario()
