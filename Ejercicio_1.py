"""Implementa una función recursiva que cuente hacia atrás (countdown) desde `n` e imprima "Despegue!" al llegar a cero.
*Solución Guiada*: Caso base: n == 0 (print). Recursivo: print(n), llamada a(n-1)."""

def countdown(n):
    if n == 0:
        print("¡Despegue!")
    else:
        print(n)
        countdown(n - 1)


countdown(5)