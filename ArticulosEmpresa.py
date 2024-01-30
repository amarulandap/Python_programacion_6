"""Programa para manejar los datos de los artículos de una empresa."""
from ValidacionDatos import *

# Función para ingresar un artículo.
def ingresarArticulo():

    while True:

        registro = [ ]                      # Almacenar los datos de cada uno de los artículos.

        codigoArticulo = ValidarEntero("\nCódigo del artículo: ", "Error, ingrese un código correcto.")
        registro.append(codigoArticulo)

        unidades = ValidarEntero("Unidades: ", "Error, ingrese una cantidad correcta.")
        registro.append(unidades)

        if unidades < 0:
            print("Error, ingrese una cantidad mayor que cero.")
            continue

        precio = ValidarEntero("Precio: ", "Error, ingrese un precio correcto.")
        registro.append(precio)

        if precio < 0:
            print("Error, ingrese un precio correcto.")
            continue

        nombreArticulo = input("Nombre del artículo: ")
        registro.append(nombreArticulo)

        return registro
        break


# Función para consultar un artículo
def consultarArticulo(matrizArticulos):

    codigoArticulo = ValidarEntero("\nCódigo del artículo: ", "Error, ingrese un código correcto.")

    encontrado = False
    for i in range(len(matrizArticulos)):                 # Recorremos la matriz de artículos.
        if codigoArticulo == matrizArticulos[i][0]:       # Validamos los valores de la primera columna.
            encontrado = True
            fila = i
            break

    if encontrado == False:
        print("\nArtículo no existe.")
    else:
        print("\nCódigo: ", matrizArticulos[fila][0],'\n',
              "Nombre: ", matrizArticulos[fila][3],'\n',
              "Unidades: ", matrizArticulos[fila][1],'\n',
              "Precio: ", matrizArticulos[fila][2])


# Función para gregar cantidad.
def agregarCantidad(matrizArticulos):

    while True:

        codigoArticulo = ValidarEntero("\nCódigo del artículo: ", "Error, ingrese un código correcto.")

        cantidad = ValidarEntero("Ingrese las unidades: ", "Error, ingrese una cantidad correcta")

        if cantidad < 0:
            print("Error, ingrese una cantidad mayor que cero.")

        encontrado = False
        for i in range(len(matrizArticulos)):
            if matrizArticulos[i][0] == codigoArticulo:
                matrizArticulos[i][1] += cantidad
                encontrado = True

        if encontrado == False:
            print("Artículo no encontrado.")

        return matrizArticulos


# Función para vender un artículo.
def venderArticulo(matrizArticulos):            # Restar la cantidad de artículos vendidos.

    codigoArticulo = ValidarEntero("\nCódigo del artículo: ", "Error, ingrese un código correcto.")

    cantidad = ValidarEntero("Ingrese las unidades: ", "Error, ingrese una cantidad correcta")

    if cantidad < 0:
        print("Error, ingrese una cantidad mayor que cero.")

    encontrado = False
    for i in range(len(matrizArticulos)):
        if matrizArticulos[i][0] == codigoArticulo:
            matrizArticulos[i][1] -= cantidad
            encontrado = True
            costoVenta = matrizArticulos[i][2] * cantidad

    if encontrado == False:
        print("Artículo no encontrado.")

    print("Total:", costoVenta)             # Indicar el costo de la venta.

    return matrizArticulos


# Función para eliminar un artículo.
def eliminarArticulo(matrizArticulos):

    codigoArticulo = ValidarEntero("\nCódigo del artículo: ", "Error, ingrese un código correcto.")

    encontrado = False
    for i in range(len(matrizArticulos)):
        if matrizArticulos[i][0] == codigoArticulo:
            del matrizArticulos[i]                  # Eliminamos el registro.
            encontrado = True

    if encontrado == False:
        print("Artículo no encontrado.")

    return matrizArticulos

# Crear el menú de opciones.
registros = [ ]                         # Es la tabla o matriz de artículos.
while True:

    print("Menú de opciones: ",'\n',
          "1. Ingresar artículo.",'\n',
          "2. Consultar artículo.",'\n',
          "3. Agregar cantidad.",'\n',
          "4. Vender.",'\n',
          "5. Eliminar artículo.",'\n',
          "6. Salir")

    opcion = ValidarEntero("Seleccione una opción: ", "Ingrese una opción correcta.")

    if opcion < 1 or opcion > 6:
        print("Ingrese una opción correcta.")
        continue

    if opcion == 1:
        registro = [ ]                          # Almacenamos los datos de cada artículo.
        registro = ingresarArticulo()
        registros = registros + [registro]      # Agregar un nuevo artículo a la tabla.

        print(registros)

    elif opcion == 2:
        consultarArticulo(registros)

    elif opcion == 3:
        registros = agregarCantidad(registros)

    elif opcion == 4:
        registros = venderArticulo(registros)    # Restamos la cantidad de unidades a vender.

    elif opcion == 5:
        registros = eliminarArticulo(registros)

    elif opcion == 6:
        print("Hasta pronto")
        break

    else:
        continue

