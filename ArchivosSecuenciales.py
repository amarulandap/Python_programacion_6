"""Continuación de la explicación de como manipular archivos secuenciales."""

from ValidacionDatos import *

# Crear una función para controlar el acceso a los archivos.
def abrirArchivo():

    while True:
        nombreArchivo = input("Nombre del archivo: ")           # pedimos el nombre del archivo a leer.

        try:
            archivo = open(nombreArchivo + '.txt', 'r')         # Abrimos el archivo para lectura.

        except FileNotFoundError:
            print("Archivo no existe")

            crearArchivo = ValidarEntero("¿Desea crear el archivo? 1. Si; 2. No.    ",
                                         "Error, ingrese la opción correcta")            # Damos la opción de crear el archivo.

            if crearArchivo == 1:
                archivo = open(nombreArchivo + '.txt', 'w')
            else:
                continue

        break

    return archivo

archivo = abrirArchivo()

# Leer el archivo.
cadenas = [ ]
for i in range(7):
    cadena = archivo.readline()
    cadenas.append(cadena)

for i in cadenas:
    print(i)
