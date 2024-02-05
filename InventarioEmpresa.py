"""
codigoArticulo. -- entero -- 5 columnas.
nombreArticulo. -- string -- 20 columnas.
precio.
cantidad. -- entero -- 6 columnas.

funciones:
1. IngresarArticulo.
2. ConsultarArticulo.
3. ComprarArticulo (sumar unidades al inventario).
4. VenderArticulo (restar unidades al inventario).
5. EliminarArticulo.
6. Salir.

Variables:
inventarioEmpresa: nombre del archivo en disco.
inventario: Objeto de tipo archivo.
lineaTexto: Línea que contiene los datos del artículo.
"""
from ValidacionDatos import *

# 1. Crear el módulo de apertura del archivo.
def aperturaArchivo():

    global inventarioEmpresa
    while True:
        inventarioEmpresa = input("Nombre del archivo sin extensión: ")       # Ingrese el nombre del archivo sin extensión.

        try:
            inventario = open(inventarioEmpresa + '.txt', 'r')                # Si el archivo ya existe, lo abrimos en modo lectura.
            inventario.close()

        except FileNotFoundError:
            print("Archivo no existe.")                                       # Damos la opción de crear el archivo.
            opcion = ValidarEntero("¿Desea crear el archivo? 1. Si ; 2. No. ", "Error, ingrese una opción correcta.")

            if opcion == 1:
                inventario = open(inventarioEmpresa + '.txt', 'w')            # Creamos el archivo con un nombre predeterminado.
                inventario.close()
            else:
                continue

        break

# 2.4. Crear el módulo para buscar la primera línea de inventario libre.
def buscarLineaLibre():
    global inventarioEmpresa

    inventario = open(inventarioEmpresa.txt, 'r')
    posicion = inventario.tell()
    lineaTexto = inventario.readline()
    encontrado = False

    while lineaTexto != '':
        [codigoArticulo, nombreArticulo, precioArticulo, cantidadArticulo] = lineaARegistro(lineaTexto)

        if codigoArticulo == 0:
            encontrado == True                                        # Encontró un espacio libre para ingresar un nuevo artículo.
            break
        posicion = inventario.tell()
        lineaTexto = inventario.readline()

    inventario.close()
    return [encontrado, posicion]


# 2.3. Crear el módulo para ingresar un artículo al inventario.
def grabarArticulo(lineaTexto):
    global inventarioEmpresa

    [encontrado, posicion] = buscarLineaLibre()

    if encontrado:
        inventario = open(inventarioEmpresa, '+r')
        inventario.seek(posicion)
        inventario.write(lineaTexto)
        inventario.close()
    else:
        inventario = open(inventarioEmpresa.txt, 'a')
        inventario.write(lineaTexto)
        inventario.close()


# 2.2. Crear el módulo para leer el código y recuperar los datos del artículo.
def lineaARegistro(lineaTexto):
    listaDatos = lineaTexto.split(',')                              # Almacenar cada uno de los datos del artículo.
    codigoArticulo = listaDatos[0]
    nombreArticulo = listaDatos[1][0:len(listaDatos[1]):1]
    precioArticulo = listaDatos[2]
    cantidadArticulo = listaDatos[3]

    return [codigoArticulo, nombreArticulo, precioArticulo, cantidadArticulo]


# 2.1. Crear el módulo para validar si el artículo ya existe.
def buscarCodigo(codigo):
    global inventarioEmpresa

    inventario = open(inventarioEmpresa.txt, 'r')
    posicion = inventario.tell()
    lineaTexto = inventario.readline()
    encontrado = False

    while lineaTexto != '':
        [codigoArticulo, nombreArticulo, precioArticulo, cantidadArticulo] = lineaARegistro(lineaTexto)

        if codigo == codigoArticulo:
            encontrado = True                                      # Indicamos que el artículo ya existe.
            break

        posicion = inventario.tell()
        lineaTexto = inventario.readline()

    inventario.close()

    return [encontrado, posicion]


# 2. Crear el módulo para ingresar los artículos.
def ingresarArticulo():

    global inventarioEmpresa

    while True:
        codigoArticulo = ValidarEntero("Código del artículo: ", "Error, ingrese un código correcto.")

        if codigoArticulo < 0 or codigoArticulo > 9999:
            print("Error, ingrese un código correcto.")
            continue

        [codigoEncontrado, posicion] = buscarCodigo(codigoArticulo)  # Llamar la función para validar si el artículo ya existe.

        if codigoEncontrado:                                        # Si ya existe el artículo, interrumpimos
            print("Código ya existe.")
            break

        nombreArticulo = input("Nombre del artículo: (Máximo 20 caractéres) ")

        precioArticulo = ValidarEntero("Precio: $", "Error, ingrese un precio correcto.")

        if precioArticulo <= 0:
            print("Error, ingrese un precio correcto.")
            continue

        cantidadArticulo = ValidarEntero("Cantidad: ", "Error, ingrese una cantida correcta.")

        if cantidadArticulo <= 0 or cantidadArticulo > 99999:
            print("Error, ingrese una cantida correcta.")
            continue

        lineaTexto = str(codigoArticulo).rjust(5) + ',' + nombreArticulo.rjust(20) + ',' + str(precioArticulo) + ',' + str(cantidadArticulo).rjust(6) + '\n'
        grabarArticulo(lineaTexto)

        break


# 3.1. Crear el módulo para leer los datos del artículo.
def leerRegistro(posicion):
    global inventarioEmpresa

    inventario = open(inventarioEmpresa.txt, 'r')
    inventario.seek(posicion)
    lineaTexto = inventario.readline()

    return lineaTexto


# 3. Crear el módulo para consultar el artículo.
def consultarArchivo():

    global inventarioEmpresa

    while True:
        codigoArticulo = ValidarEntero("Código del artículo: ", "Error, ingrese un código correcto.")

        if codigoArticulo < 0 or codigoArticulo > 9999:
            print("Error, ingrese un código correcto.")
            break
        else:
            [encontrado, posicion] = buscarCodigo(codigoArticulo)

            if encontrado:
                lineaTexto = leerRegistro(posicion)
                [codigoArticulo, nombreArticulo, precioArticulo, cantidadArticulo] = lineaARegistro(lineaTexto)
                print("Código: ", codigoArticulo,'\n',
                      "Nombre: ", nombreArticulo.strip(), '\n',
                      "Precio: ", precioArticulo, '\n',
                      "Cantidad: ", cantidadArticulo)
            else:
                print("Artículo no existe.")

        break


# 4.1. Crear el módulo para actualizar la cantidad de artículos.
def actualizarRegistro(posicion, cantidad):
    global inventarioEmpresa

    lineaTexto = leerRegistro(posicion)
    [codigoArticulo, nombreArticulo, precioArticulo, cantidadArticulo] = lineaARegistro(lineaTexto)
    cantidadArticulo += cantidad
    lineaTexto = str(codigoArticulo).rjust(5) + ',' + nombreArticulo.rjust(20) + ',' + str(precioArticulo) + ',' + str(cantidadArticulo).rjust(6) + '\n'
    inventario = open(inventarioEmpresa.txt, 'r+')
    inventario.sekk(posicion)
    inventario.write(lineaTexto)
    inventario.close()

# 4. Crear el módulo para la compra de los artículos.
def comprarArticulo():
    global inventarioEmpresa

    while True:
        codigoArticulo = ValidarEntero("Código del artículo: ", "Error, ingrese un código correcto.")

        if codigoArticulo < 0 or codigoArticulo > 9999:
            print("Error, ingrese un código correcto.")
            break
        else:
            [encontrado, posicion] = buscarCodigo(codigoArticulo)

        if encontrado:
            cantidadComprada = ValidarEntero("Cantidad comprada: ", "Error, ingrese una cantidad correcta.")

            if cantidadComprada < 0:
                print("Error, ingrese una cantidad correcta.")
                break
            else:
                actualizarRegistro(posicion, cantidadComprada)
        else:
            print("Artículo no existe.")


# 5. Crear el módulo para la venta de los artículos.
def venderArticulo():
    global inventarioEmpresa

    while True:
        codigoArticulo = ValidarEntero("Código del artículo: ", "Error, ingrese un código correcto.")

        if codigoArticulo < 0 or codigoArticulo > 9999:
            print("Error, ingrese un código correcto.")
            break
        else:
            [encontrado, posicion] = buscarCodigo(codigoArticulo)

        if encontrado:
            lineaTexto = leerRegistro(posicion)
            [codigoArticulo, nombreArticulo, precioArticulo, cantidadArticulo] = lineaARegistro(lineaTexto)

            cantidadVendida = ValidarEntero("Cantidad a vender: ", "Error, ingrese una cantidad correcta.")

            if cantidadVendida > cantidadArticulo:
                print("cantidad no disponible.")
                break
            else:
                actualizarRegistro(posicion, -cantidadVendida)
        else:
            print("Artículo no existe.")


# 6.1. Módulo para eliminar los registros.
def eliminarRegistro(posicion):
    global inventarioEmpresa

    lineaTexto = leerRegistro(posicion)
    [codigoArticulo, nombreArticulo, precioArticulo, cantidadArticulo] = lineaARegistro(lineaTexto)
    codigoArticulo = 0
    lineaTexto = str(codigoArticulo).rjust(5) + ',' + nombreArticulo.rjust(20) + ',' + str(precioArticulo) + ',' + str(cantidadArticulo).rjust(6) + '\n'
    inventario = open(inventarioEmpresa.txt, 'r+')
    inventario.seek(posicion)
    inventario.write(lineaTexto)
    inventario.close()


# 6. Crear el módulo para eliminar los artículos.
def eliminarArticulo():
    global inventarioEmpresa

    while True:
        codigoArticulo = ValidarEntero("Código del artículo: ", "Error, ingrese un código correcto.")

        if codigoArticulo < 0 or codigoArticulo > 9999:
            print("Error, ingrese un código correcto.")
            break
        else:
            [encontrado, posicion] = buscarCodigo(codigoArticulo)

        if encontrado:
            eliminarRegistro(posicion)
        else:
            print("Artículo no existe.")

# Programa principal.
aperturaArchivo()                       # Abrimos o creamos el archivo de datos.

while True:

    print('\n',"Menú de opciones:",'\n',
          "1. Ingresar artículo.",'\n',
          "2. Consultar artículo.",'\n',
          "3. Comprar artículo.",'\n',
          "4. Vender artículo.",'\n',
          "5. Eliminar artículo.", '\n',
          "6. Salir")

    opcion = ValidarEntero("Seleccione una opción: " , "Error, seleccione una opción correcta.")

    if opcion == 1:
        ingresarArticulo()

    elif opcion == 2:
        consultarArchivo()

    elif opcion== 3:
        comprarArticulo()

    elif opcion == 4:
        venderArticulo()

    elif opcion == 5:
        eliminarArticulo()

    elif opcion == 6:
        break

    else:
        continue