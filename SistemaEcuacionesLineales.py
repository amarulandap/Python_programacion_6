"""Resolver un sistema de ecuaciones lineales usando Numpy.

    AX = B
    A : matriz de coeficientes.
    B : matriz de constantes.
    X : vector solución.

    X = matriz inversa de A * B. --> |A| != 0.
"""

import numpy as np
from random import *
from ValidacionDatos import ValidarEntero

# Construir la matriz de coeficientes.
A = np.array([[2, 4, 5], [3, 1, 4], [5, 2, 4]])

# Construir la matriz de constantes.
B = np.array([[5], [6], [7]])

# verificamos que el determinante de A sea diferente de Zero.
determinanteA = np.linalg.det(A)

if determinanteA == 0:
    print("El determinante de A es 0.")
else:
    # Calculamos la inversa de A
    inversaA = np.linalg.inv(A)

    # Multiplicamos la transpuesta de A con B.
    X = np.dot(inversaA,B)

    print("Solución del sistema de ecuaciones: \n",
          X)

# En lugar de calcular la inversa, usamos el método solve de numpy.
np.set_printoptions(precision = 4)
X1 = np.linalg.solve(A,B)

print("Solución alternativa del sistema de ecuaciones: \n",
          X1)




"""Programa para crear un vector con la suma de las filas de una matriz"""

def sumarFilas(matriz):

    listaSuma = [ ]                             # Lista para almacenar los resultados de las sumas.

    # Calcular la suma de cada una de las filas.
    for i in range(matriz.shape[0]):
        suma = 0
        for j in range(matriz.shape[1]):
            suma += matriz[i, j]

        listaSuma.append(suma)                  # Agregar el resultado de cada suma a la lista.

    vectorSuma = np.array(listaSuma)

    return vectorSuma


# Pedir el número de filas y de columnas.
while True:
    print('\n')
    filas = ValidarEntero("Filas de la matriz: ", "Error, ingrese una cantidad correcta")
    columnas = ValidarEntero("Columnas de la matriz: ", "Error, ingrese una cantidad correcta")

    if filas <= 0 or columnas <= 0:
        print("Error, ingrese una cantidad correcta.")
    else:
        break

# Crear una matriz de números enteros.
lista1 = [ ]
for i in range(filas):
    fila = [ ]
    for j in range(columnas):
        fila = fila + [randint(0, 50)]

    lista1 = lista1 + [fila]

matriz1 = np.array(lista1)
print(matriz1)

# Creamos un vector para recibir los resultados de la sumas.
listaSuma = [ ]
vectorSuma = np.array(listaSuma)

vectorSuma = sumarFilas(matriz1)
print("Vector sumas: ",vectorSuma)




"""Programa para generar el triangulo de pascal."""

# Pedir el número de filas y columnas.
while True:
    filasPascal = ValidarEntero("\nFilas triangulo: ", "Error, ingrese una cantidad correcta.")

    if filasPascal <= 0:
        print("Error, ingrese una cantidad correcta.")
    else:
        break

# Generamos la matriz cuadrada y nula.
matrizPascal = np.zeros([filasPascal,filasPascal], int)

for i in range(filasPascal):
    matrizPascal[i,0] = 1
    matrizPascal[i,i] = 1

for i in range(2,filasPascal):
    for j in range(1,filasPascal):
        matrizPascal[i,j] = matrizPascal[i-1,j-1] + matrizPascal[i-1,j]

print("Triangulo de Pascal: ",'\n',
      matrizPascal)

