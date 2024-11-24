from utilitarias_rh import validar


def eliminarRegistro(nombre, apellido): # void 
    posicion = 0 # int
    fila_columna = [0, 0] # arreglo uni int
    texto_binario = [] #arreglo bi str
    archivo = object # objeto
    
    archivo = validar["leerArchivo"]("personal.bin")
    
    if (archivo == None):
        print("Object file -- does not exist")
        return 
        
    posicion = buscar(archivo, nombre, apellido)
    if posicion == None:
        return
    fila_columna = determinarTamaño(archivo)
    texto_binario = iniTextoBinario(fila_columna[0])
    valoresArregloBinario(texto_binario, archivo)
    archivo.close()
    
    archivo = validar["escribirArchivo"]("personal.bin")
    if (archivo == None):
        print("Object file -- does not exist")
        return 
    
    for i in range(len(texto_binario)):
        if i != posicion:
            archivo.write(texto_binario[i].encode("utf-8"))
    
    archivo.close()
    return



def buscar(archivo, nombre, apellido): # int
    if (archivo == None):
        print("Object file -- does not exist")
        return
    
    n = 0 # int
    band = True # bool
    archivo.seek(0)
    for i in archivo:
        fila = i.decode("utf-8").split("#")
        if (str(fila[0].lower()) == nombre.lower() and str(fila[1].lower()) == apellido.lower()):
            band = False
            return n
        n += 1
    if band:
        print("El empleado {} {} no se encuentra registrado".format(nombre, apellido))
        return None
    
    
def generarLinea(arreglo): # str
    linea = ""
    for i in range(len(arreglo)):
        if i != (len(arreglo) - 1):
            linea += "{}#".format(arreglo[i])
        else:
            linea += arreglo[i]
    return linea


def determinarTamaño(archivo): # arreglo uni int
    
    if (archivo == None):
        print("Object file -- does not exist")
        return [0, 0]
    
    archivo.seek(0)
    fila = 0 # int
    columna = 0 # int
    bandera = True # bool
    fila_columna = [0,0] # arreglo uni int
    campo = [] # arreglo uni str
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
    return fila_columna

    
def iniTextoBinario(filas): # arreglo uni str
    if filas > 0:
        return ["e" for i in range(filas)]
    
    
def valoresArregloBinario(arreglo, archivo): # void
    if (archivo == None):
        print("Object file -- does not exist")
        return 
    
    archivo.seek(0)
    indice = 0 # int
    for i in archivo:
        fila = i.decode("utf-8").split("#")
        fila = generarLinea(fila)
        arreglo[indice] = fila
        indice += 1
    return 


eliminarRegistro("abisaac", "carmona")