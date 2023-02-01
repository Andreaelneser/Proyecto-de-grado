import glob
import os

#la función retorna lista con todos los archivos de una carpeta
def lista_archivos(carpeta):
    return glob.glob(carpeta + "/*.fits")

#la función retorna una lista con los archivos que contienen una determinada cadena de texto
def archivos_con_cadena(lista_archivos, cadena):
    return [archivo for archivo in lista_archivos if cadena in archivo]

#la funcion elimina los archivos de una lista de archivos
def eliminar_archivos(lista_archivos):
    for archivo in lista_archivos:
        os.remove(archivo)


#main del programa
if __name__ == "__main__":
    carpeta = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar"
    lista_archivos = lista_archivos(carpeta)
    archivos_con_cadena = archivos_con_cadena(lista_archivos, "(1)")
    eliminar_archivos(archivos_con_cadena)


        

