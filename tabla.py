import pathlib
import pandas as pd 
import glob
import numpy as np

#recorrer carpeta DatosCSV
path = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/"

lines = glob.glob(path + "*.csv") #Se lee el archivo aorkeys.txt y se guarda en una lista

f = open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/ConT.csv", "w")

for line in lines: #Recorre la lista lines
    nombrearchivo = str(line)
    print(nombrearchivo)

    if nombrearchivo.count('_') == 3:
        f.write(str(nombrearchivo)+'\n')


f.close()

'''nombrearchivo = str(filename)
        aorkey = nombrearchivo[71:]
        f = open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/LineayFile.csv", "a")
        f.write("Linea: ")
        f.write(str(line))
        f.write("\n")
        f.write("File: ")
        f.write(str(aorkey))

        #datos = pd.read_csv(filename, header=None, delimiter=';')
        #if line == aorkey:
        #    f = open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/Archivos.csv", "a")
        #    f.write(str(filename))
        #    f.write('\n')

        datos = datos[1].values.reshape(-1, 1).T
        f = open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/ColumnaB.csv", "a")
        f.write(str(datos))
        f.write('\n')'''
