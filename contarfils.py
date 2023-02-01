import pathlib
import pandas as pd 
import numpy as np

#recorrer carpeta DatosCSV
path = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV"

f = open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/zCantidadSoloAor.csv", "a")
f.write('Aorkey' + ';' + 'Número de filas')
f.write('\n')

for filename in pathlib.Path(path).glob("*.csv"):
    datos = pd.read_csv(filename, header=None, delimiter=';')
    columna = datos.shape[0]
    nombrearchivo = str(filename)
    indicefits = nombrearchivo.index('.fits')
    aorkey = nombrearchivo[71:indicefits]
    #print(aorkey)
    f = open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/zCantidadSoloAor.csv", "a")
    f.write(str(aorkey) + ';')
    f.write(' ')
    f.write(' ')
    f.write(' ')
    f.write(str(columna))
    f.write('\n')
    f.close()







