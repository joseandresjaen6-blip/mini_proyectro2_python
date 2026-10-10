""" Invierte una cadena recursivamente.
*Solución*: Caso base cadena vacía. Recursivo: `invertir(cadena[1:]) + cadena[0]`."""

def invertir(cadena):
    if cadena == "":
        return cadena
    else:
        return invertir(cadena[1:]) + cadena[0]


palabra = "Python"
print(invertir(palabra))