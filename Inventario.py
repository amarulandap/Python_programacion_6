"""Aplicación para almacenar en disco y listar los articulos de una empresa."""

from ValidacionDatos import *

# definir el nombre del archivo en disco y del objeto de tipo archivo para leerlo.
def abrirArchivo():

    while True:
        nombreArchivo = input("Ingrese el nombre del Archivo: ")

        try:
            inventario = open(nombreArchivo + '.txt', 'r')           # Leer el objeto de tipo archivo.

        except FileNotFoundError:
            print("\nEl archivo no existe")
            crear = ValidarEntero("¿Desea crear el archivo? 1. Si ; 2. No. : ", "Error, seleccione una opción correcta")

            if crear == 1:
                inventario = open(nombreArchivo + '.txt', 'w')       # Crear el objeto de tipo archivo.
            else:
                continue

        break

    return inventario, nombreArchivo                                              # Retornamos el objeto de tipo archivo.


# Función para ingresar los datos de cada artículo.
def ingresarArticulo(datosArticulo):

    while True:
        codigoProducto = ValidarEntero("\nCódigo del producto: ", "Error, ingrese un código correcto.")
        datosArticulo.append(codigoProducto)

        nombreProducto = input("Nombre del producto: ")
        datosArticulo.append(nombreProducto)

        precioArticulo = ValidarEntero("Precio: $", "Error, ingrese un precio correcto.")

        if precioArticulo <= 0:
            print("Error, ingrese un precio correcto.")
            continue
        else:
            datosArticulo.append(precioArticulo)

        cantidadArticulo = ValidarEntero("Cantidad: ", "Error, ingrese una cantidad correcta.")

        if cantidadArticulo < 0:
            print("Error, ingrese una cantidad correcta.")
            continue
        else:
            datosArticulo.append(cantidadArticulo)

        break

    return datosArticulo


""" Programa Principal """

# llamar la función para abrir el archivo.
inventario, nombreArchivo = abrirArchivo()

# Crear el menú principal.
while True:

    print('\n',"\tMenú de opciones: ",'\n',
          "1. Ingresar artículo.",'\n',
          "2. Listar artículos.",'\n',
          "3. Salir.", '\n')
    opcion = ValidarEntero("Seleccione una opción: ", "Error, seleccione una opción correcta.")

    if opcion == 1:
        datosArticulo = []                                  # definir la lista para almacenar los datos de los artículos.
        datosArticulo = ingresarArticulo(datosArticulo)     # Llamar la función para ingresar los datos del artículo.
        inventario = open(nombreArchivo + '.txt', 'a')
        lineaTexto = "Código: " + str(datosArticulo[0]) + " Nombre: " + str(datosArticulo[1]) + " Precio: $" + str(datosArticulo[2]) + " Cantidad: " + str(datosArticulo[3]) + "\n"
        inventario.write(lineaTexto)
        inventario.close()                                  # Cerrar para que los datos se envíen al archivo.

    elif opcion == 2:
        inventario, nombreArchivo = abrirArchivo()                         # Abrimos el archivo en modo lectura.
        inventario = open(nombreArchivo + '.txt', 'r')
        lineaTexto = inventario.readline()
        while lineaTexto != '':
            datosArticulo = lineaTexto.split(' , ')                        # leer línea por línea el archivo.
            print(datosArticulo)
            lineaTexto = inventario.readline()

        inventario.close()

    elif opcion == 3:
        print("Hasta pronto.")
        break

    else:
        continue


