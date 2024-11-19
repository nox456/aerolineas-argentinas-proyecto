def listar(archivo):  # void
    if archivo != None:
        print(
            "---------------------------------------------------------------------------------------------------"
        )
        print(
            "{0:10}  {1:10}  {2:8}  {3:2}  {4:20}  {5:25}  {6:7}".format(
                "Nombre",
                "Apellido",
                "Cédula",
                "Edad",
                "Fecha de Nacimiento",
                "Cargo",
                "Salario",
            )
        )
        for fila in archivo:
            campos = fila.decode("utf-8").split("#")
            print(
                "{0:10}  {1:10}  {2:7}  {3:<4}  {4:<20}  {5:25}  {6:,} $".format(
                    campos[0],
                    campos[1],
                    int(campos[2]),
                    int(campos[3]),
                    int(campos[4]),
                    campos[5],
                    int(campos[6]),
                )
            )
        print(
            "---------------------------------------------------------------------------------------------------"
        )


recursos_humanos = {"listar": listar}
