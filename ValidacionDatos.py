import sys

def ValidarEntero(mensaje, mensaje1):

    while True:
        try:
            entero = int(input(mensaje))
            return entero
        except ValueError as e:
            print(mensaje1)
            # sys.exit()
            continue
        break

def ValidarReal(mensaje, mensaje1):

    while True:
        try:
            real = float(input(mensaje))
            return real
        except ValueError as e:
            print(mensaje1)      # File = sys.stderr.
            # sys.exit()
            continue
        break