"""Encuentra el número máximo en una lista recursivamente.
*Solución*: Compara el primer elemento con el máximo del resto de la lista `max(lista[0], recursivo(lista[1:]))`."""


def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0], maximo(lista[1:]))


numeros = [12, 5, 28, 9, 17]
print(maximo(numeros))