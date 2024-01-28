"""1. Programa para buscar un elemento en una matriz."""

from random import *
from ValidacionDatos import *
from numpy import *

# 1. Generar una matriz de 4 x 4 con números aleatorios en un rango especifico.
matrizAleatorios = [ ]
for i in range(0, 4, 1):
    filasAleatorios = [ ]
    for j in range(0, 4, 1):
        filasAleatorios = filasAleatorios + [randint(1, 20)]

    matrizAleatorios = matrizAleatorios + [filasAleatorios]

# 2. Convertir la matriz en un arreglo.
matrizAleatorios = array(matrizAleatorios)

# 2. Pedir que se ingrese el número a buscar.
while True:
    numeroBuscar = ValidarEntero("Ingrese un número entre 1 y 20: ", "Error, ingrese una cantidad correcta.")

    if numeroBuscar < 1 or numeroBuscar > 20:
        print("Error, ingrese una cantidad correcta.")
        continue

    break

encontrado = False
for i in range(4):
    for j in range(4):
        if matrizAleatorios[i][j] == numeroBuscar:
            encontrado = True

if encontrado == True:
    print("Número ", numeroBuscar, " pertenece a la Matriz.")
else:
    print("Número ", numeroBuscar, " no pertenece a la Matriz.")

print('\n',matrizAleatorios)




"""2. Programa para generar el juego del laberinto."""

# 1. Definir las dimensiones del laberinto.
while True:
    filasLaberinto = ValidarEntero("\nIngrese el número de filas del laberinto: ", "Error, ingrese una cantidad correcta.")
    columnasLaberinto = ValidarEntero("\nIngrese el número de columnas del laberinto: ", "Error, ingrese una cantidad correcta.")

    if filasLaberinto <= 0 or columnasLaberinto <= 0:
        print("Error, ingrese una cantidad correcta.")
        continue

    break

# 2. Generar la matriz con todos los bordes == 1 y al interior con valores 0 o 1.
laberinto = [ ]                                 # Defino el arreglo para crear el laberinto.

for i in range(filasLaberinto):
    fillab = [ ]                                # Defino cada una de las filas de la matriz.
    for j in range(columnasLaberinto):          # Llenar cada una de las filas de la matriz.
        if i == 0 or i == (filasLaberinto - 1) or j == 0 or j == (columnasLaberinto - 1):
            fillab = fillab + [1]
        else:
            fillab = fillab + [randint(0, 1)]

    laberinto = laberinto + [fillab]

laberinto = array(laberinto)        # Convierto en matriz.
print("laberinto: \n",
      laberinto)




"""3. Programa para administrar el uso de los casilleros de un club."""

def asignarCasillero(casillero):                # Recorrer la matriz buscando posiciones libres (con valor 0).
    asignado = False
    for i in range(casillero.shape[0]):
        if asignado == True:
            break
        for j in range(casillero.shape[1]):
            if casillero[i, j] == 0:
                casillero[i, j] = ValidarEntero("\nCódigo del usuario: ", "Error, ingrese un código correcto.")
                print("Casillero ", i * 10 + j, "asignado.")
                asignado = True
                break

def devolverCasillero(casillero):
    codigoUsuario = ValidarEntero("\nCódigo del usuario: ", "Error, ingrese un código correcto.")
    for i in range(casillero.shape[0]):
        for j in range(casillero.shape[1]):
            if casillero[i, j] == codigoUsuario:
                casillero[i, j] = 0
                print("Casillero libre.")

    print("Usuario no encontrado.")

def consultarCasillero(casillero):
    fila = ValidarEntero("\nPrimer dígito del número del casillero: ", "Error, ingrese un dígito correcto.")
    columna = ValidarEntero("Segundo dígito del número del casillero: ", "Error, ingrese un dígito correcto.")

    if casillero[fila, columna] == 0:
        print("Casillero libre.")
    else:
        usuario = casillero[fila, columna]
        print("Casillero ocupado por el usuario de código: ",usuario)


def consultarUsuario(casillero):
    codigoUsuario = ValidarEntero("\nCódigo del usuario: ", "Error, ingrese un código correcto.")

    for i in range(casillero.shape[0]):
        for j in range(casillero.shape[1]):
            if casillero[i, j] == codigoUsuario:
                print("El usuario tiene asignado el casillero ",i * 10 + j)

    print("El usuario no tiene casillero asignado.")


# 1. Crear la matriz para los casilleros de 10 x 10.
listaCasillero = [ ]                             # Defino la lista.
casillero = array(listaCasillero)                # Convierto en un arreglo.

casillero = zeros([10,10], int)       # Generamos la matriz nula.

while True:

    # 2. Imprimimos en pantalla el menú.
    print("\n 1. Asignar casillero.",'\n',
          "2. Devolver casillero.",'\n',
          "3. Consultar casillero.",'\n',
          "4. Consultar usuario.",'\n',
          "5. Salir")

    opcion = ValidarEntero("Seleccione una opción: ", "Error, ingrese una opción correcta.")
    if opcion < 1 or opcion > 5:
        print("Error, ingrese una opción correcta.")
        continue

    if opcion == 1:
        asignarCasillero(casillero)
    elif opcion == 2:
        devolverCasillero(casillero)
    elif opcion == 3:
        consultarCasillero(casillero)
    elif opcion == 4:
        consultarUsuario(casillero)
    elif opcion == 5:
        print("Adios.")
        break
    else:
        continue





