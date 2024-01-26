from random import *
from numpy import *

#Para crear una matriz.
matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
print("Matriz 1:",matriz1)


# Para acceder a un elemento en particular.
print(matriz1[2][1])


# Para acceder a los elementos de una fila.
print("Fila 0:",matriz1[0])


# Para acceder a los elementos de una columna.
print("Columna1:")
for i in range(3):
    print(matriz1[i][1])


# Para visualizarla por filas.
print("\nMatriz por filas: ")
for i in range(3):
    print(matriz1[i])


# Declaraciones implicitas. (El rango me indica el número de filas y las operaciones dentro de la llave, el de columnas.)
matriz2 = [[i] for i in range(9)]
print("Matriz 2:",matriz2)

matriz3 = [[i,i+2] for i in range(6)]
print("Matriz3:",matriz3)

matriz4 = [[i, i+3, i+5] for i in range(4)]
print("Matriz 4:")
for j in range(4):
    print(matriz4[j])

# Declaraciones explicitas.
matriz5 = [ ]
for i in range(3):
    fila = [ ]                              # Declaramos cada una de las filas.
    for j in range(3):
        fila = fila + [randint(0,9)]  # Concatenamos el contenido de la fila con un nuevo número.
    matriz5 = matriz5 + [fila]

print("\n Matriz de números aleatorios:")
for i in range(3):
    print(matriz5[i])

"""Funciones del modulo numpy"""

# Convertir las listas en arreglos.
# Para crear un vector, primero se debe definir una lista, y para crear una matriz, se debe definir una lista de listas.
arreglo1 = array(matriz1)
print('\n',"Arreglo 1:",'\n',arreglo1)


# Para especificar el tipo de dato.
arreglo2 = array(matriz2, float)
print('\n', "Arreglo 2:", arreglo2)


# Para acceder a un elemento del arreglo.
print('\n',"Elemento (1,0) del arreglo 2:", arreglo2[1,0])


# Para obtener una fila o columna completa del arreglo.
print('\n',"Fila 2 del arreglo 1:",'\n',arreglo1[2,:])
print('\n',"Columna 2 del arreglo 1:",'\n',arreglo1[:,2])


# Para obtener las dimensiones de un arreglo.
[filasArreglo, columnasArreglo] = arreglo1.shape
print("\nDimensiones del arreglo 1: ",filasArreglo,'x',columnasArreglo)


# Operador de pertenencia.
pertenece = 11 in arreglo2
if pertenece:
    print("11 pertenece al arreglo 2")
else:
    print("11 no pertenece al arreglo 2")


# Generar un vector con un rango.
arreglo3 = array(range(9), int)
print('\n', "Arreglo 3 generado por rango:", arreglo3)


#Convertir el arreglo 3 en uno de dos dimensiones.
arreglo4 = arreglo3.reshape((3,3))
print('\n',"Arreglo 3 convertido en uno de 2 dimensiones: ",'\n',arreglo4)


# Para convertir un arreglo en una lista.
lista1 = arreglo3.tolist()
print('\n',"Arreglo 3 convertido en lista: ",lista1)


# Para rellenar una matriz con un único valor usamos la función fill de numpy.
# arreglo3.fill(9)


# Concatenar listas.
lista2 = [[1,2], [3,4]]
lista3 = [[5,6], [7,8]]
print("Listas 2 y 3 concatenadas: ",lista2 + lista3)


# Convertir ambas listas en matrices y realizaremos las 4 operciones aritméticas.
arreglo5 = array(lista2)
arreglo6 = array(lista3)

print("arreglo 5 + arreglo 6:\n",arreglo5 + arreglo6)
print("\narreglo 5 - arreglo 6:\n",arreglo5 - arreglo6)
print("\narreglo 5 * arreglo 6 (elemento * elemento):\n",arreglo5 * arreglo6)

# Por ejemplo el elemento 1,1 = primera fila * primera columna, sumando los dos productos.
print("\nMultiplicar ambas matrices: \n",dot(arreglo5,arreglo6))


# Para sumar todos los elementos de una matriz.
print('\nArreglo 1:\n',arreglo1)
print("la suma de los elementos del arreglo 1 es: ",sum(arreglo1))
print("El producto de los elementos del arreglo 1 es: ",prod(arreglo1))
print("la media aritmética de los elementos del arreglo 1 es: ",mean(arreglo1))
print("la desviación estandar de los elementos del arreglo 1 es: ",format(std(arreglo1),".3f"))


# Para ordenar una matriz por filas.
arreglo7 = array(matriz5)
print("\nMatriz ordenada por filas:",sort(arreglo7))


# Para obtener la diagona de la matriz.
print("Matriz 5:\n",arreglo7,'\n',
      "Diagonal de la matriz 5: \n",diagonal(arreglo7))


# Para hallar el determinante de una matriz.
print('\n',
      "Determinante de la matriz 5(Arreglo 7): ", format(linalg.det(arreglo7),".4f"))


# Para hallar la matriz inversa.
print('\n',
      "Inversa de la matriz 5: ",linalg.inv(arreglo7))


# Para hallar la matriz transpuesta.
print('\n',
      "Transpuesta de la matriz 5: ", transpose(arreglo7))


# Para hallar la matriz triangular inferior.
print('\n',
      "Triangular inferior: \n",tril(arreglo7))


# Para hallar la matriz triangular superior.
print('\n',
      "Triangular superior: \n",triu(arreglo7))


# Para llenar una matriz de zeros.
listaNula = [ ]
matrizNula = array(listaNula)
matrizNula = zeros([4,5], int)
print("\n Matriz nula:",'\n',
      matrizNula)


# Hallar la matriz identidad con numeros reales y con numeros enteros.
print('\n',
      "Matriz identidad real: \n", identity(4))

print('\n',
      "Matriz identidad entera: \n", identity(4, int))
