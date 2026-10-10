"""1. Objetivo
Crear una clase llamada ExploradorRecursivo con tres métodos recursivos: 
imprimir_arbol(), buscar_archivo() y contar_archivos(). 
El sistema de archivos se representa mediante diccionarios anidados de Python.
"""

class ExploradorRecursivo:
    """
    Explora un sistema de archivos representado
    mediante un diccionario anidado, usando recursividad.
    """

    # --------------------------------------------------
    # PUNTO 1: IMPRIMIR EL ARBOL DE DIRECTORIOS
    # --------------------------------------------------

    @staticmethod
    def imprimir_arbol(sistema, nivel=0):
        """
        Imprime carpetas y archivos con indentacion
        segun el nivel de profundidad.
        """

        for nombre, contenido in sistema.items():
            espacio = "    " * nivel

            if isinstance(contenido, dict):
                print(f"{espacio}[CARPETA] {nombre}/")

                # CASO RECURSIVO:
                # Entramos en la carpeta y aumentamos el nivel.
                ExploradorRecursivo.imprimir_arbol(
                    contenido, nivel + 1
                )

            else:
                # CASO BASE:
                # Encontramos un archivo y lo imprimimos.
                print(f"{espacio}[ARCHIVO] {nombre}")

    # --------------------------------------------------
    # PUNTO 2: BUSCAR UN ARCHIVO
    # --------------------------------------------------

    @staticmethod
    def buscar_archivo(sistema, nombre, ruta=""):
        """
        Busca un archivo en todas las carpetas.
        Devuelve su ruta completa o None si no existe.
        """

        for elemento, contenido in sistema.items():

            # Construimos la ruta del elemento actual.
            if ruta:
                ruta_actual = f"{ruta}/{elemento}"
            else:
                ruta_actual = elemento

            if isinstance(contenido, dict):

                # CASO RECURSIVO:
                # Buscamos dentro de la carpeta encontrada.
                resultado = ExploradorRecursivo.buscar_archivo(
                    contenido, nombre, ruta_actual
                )

                # Si se encontro, devolvemos la ruta.
                if resultado is not None:
                    return resultado

            else:
                # CASO BASE:
                # Comparamos el nombre del archivo buscado.
                if elemento == nombre:
                    return ruta_actual

        # CASO BASE:
        # Si terminamos de revisar el diccionario sin
        # encontrar el archivo, devolvemos None.
        return None

    # --------------------------------------------------
    # PUNTO 3: CONTAR TODOS LOS ARCHIVOS
    # --------------------------------------------------

    @staticmethod
    def contar_archivos(sistema):
        """
        Cuenta los archivos de todas las carpetas.
        Las carpetas no se incluyen en el conteo.
        """

        total = 0

        for contenido in sistema.values():

            if isinstance(contenido, dict):

                # CASO RECURSIVO:
                # Sumamos los archivos de la subcarpeta.
                total += ExploradorRecursivo.contar_archivos(
                    contenido
                )

            else:
                # CASO BASE:
                # Cada archivo encontrado suma uno.
                total += 1

        return total


# --------------------------------------------------
# SISTEMA DE ARCHIVOS DEL EJEMPLO DEL MAESTRO
# --------------------------------------------------

sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}


# --------------------------------------------------
# PRUEBAS Y EJECUCION DEL PROGRAMA
# --------------------------------------------------

if __name__ == "__main__":

    # PRUEBA 1: IMPRIMIR EL ARBOL
    print("===== ARBOL DE DIRECTORIOS =====")
    ExploradorRecursivo.imprimir_arbol(sistema_archivos)

    # PRUEBA 2: BUSCAR UN ARCHIVO EXISTENTE
    print("\n===== BUSQUEDA DE ARCHIVO =====")

    nombre_buscado = "perro.jpg"

    resultado = ExploradorRecursivo.buscar_archivo(
        sistema_archivos, nombre_buscado
    )

    if resultado is not None:
        print(f"Archivo encontrado: {resultado}")
    else:
        print(f"El archivo '{nombre_buscado}' no existe.")

    # PRUEBA ADICIONAL: BUSCAR UN ARCHIVO INEXISTENTE
    nombre_buscado = "tarea.pdf"

    resultado = ExploradorRecursivo.buscar_archivo(
        sistema_archivos, nombre_buscado
    )

    if resultado is not None:
        print(f"Archivo encontrado: {resultado}")
    else:
        print(f"El archivo '{nombre_buscado}' no existe.")

    # PRUEBA 3: CONTAR LOS ARCHIVOS
    print("\n===== CONTEO DE ARCHIVOS =====")

    total = ExploradorRecursivo.contar_archivos(
        sistema_archivos
    )

    print(f"Cantidad total de archivos: {total}")