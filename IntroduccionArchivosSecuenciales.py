"""
archivo : Objeto creado de tipo archivo.
texto : Archivo creado en el disco.

w : Crear el archivo y agregar datos.
a : Agregar datos al archivo.
r : Leer los datos del archivo.
r+ : Leer y escribir en el archivo.
"""

archivo = open('texto.txt', 'w')                            # Crear el archivo.

cadena = "Hola mundo de los archivos secuenciales.\n"       # Escribir una cadena de texto en el archivo.
archivo.write(cadena)
cadena = "Soy Andres Marulanda\n"
archivo.write(cadena)
cadena = "Soy programador y desarrollador web\n"
archivo.write(cadena)

archivo.close()                                             # Cerramos el archivo para que los datos sean enviados.

archivo1 = open('texto.txt', 'r')                           # Leer el archivo.

cadena1 = archivo1.readline()                               # Leer cada una de las líneas de texto.
cadena2 = archivo1.readline()
cadena3 = archivo1.readline()

print(cadena1,cadena2,cadena3)                              # Imprimimos las líneas que contiene el archivo.

archivo1.close()

# Vamos a agregar registros numéricos.
registro = [123, 20, 85000, 'Los cuentos de la mamá grande']

archivo1 = open('texto.txt', 'a')
lineaTexto = "Código: " + str(registro[0]) + " Cantidad: " + str(registro[1]) + " Precio: " + str(registro[2]) + " Nombre: " + str(registro[3]) + "\n"
archivo1.write(lineaTexto)
archivo1.close()





