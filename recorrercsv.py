import pathlib
import csv 
import numpy as np

#recorrer carpeta DatosCSV
path = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV"
for filename in pathlib.Path(path).glob("*.csv"):
    #recorrer y guardar columna B de cada archivo en un nuevo archivo
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(row[1])
            with open('C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/ColumnaB.csv', 'a') as f:
                f.write(row[1] + "")