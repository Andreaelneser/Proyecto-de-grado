import os
import pathlib
import pandas as pd
import glob
import itertools
import csv
import numpy as np

path = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/"
'''
columnafinal = [0]

for filename in glob.glob(path + "/*.csv"):
    #print(filename)
    temp = pd.read_csv(filename, header=None, delimiter=';', float_precision='round_trip')
    #temp = temp.astype(float)
    columnatemp = (temp[0].values) 
    columnalistatemp = list(columnatemp)
    columnafinal = list(itertools.chain(columnafinal, columnalistatemp))
    #columnafinal.sort()
    columnafinal = list(set(columnafinal))

columnafinal.sort()

columnafinall = columnafinal

with open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/TablaFinall.csv","w") as f:
    #wr = csv.writer(f,delimiter=";")
    wr = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=";")
    wr.writerow(['{:1.18e}'.format(x) for x in columnafinall])
    #wr.writerow(columnafinal)'''


df = pd.read_csv("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/TablaFinall.csv", header=None, delimiter=';')
carac = df.values #ndarray
print(carac)

with open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/TablaFinall.csv","w") as f:
    carac = set(carac.flatten())
    carac = list(carac)
    carac.sort()
    wr = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=";")
    wr.writerow(['{:1.18e}'.format(x) for x in carac])


f= open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/TablaFinall.csv","a")

for filename in pathlib.Path(path).glob("*.csv"):
    lectura = pd.read_csv(filename, header=None, delimiter=';')
    print(type(lectura))
    '''
    columna = lectura[0].values #ndarray
    columna = list(columna) #lista
    nombrearchivo = str(filename)
    indicefits = nombrearchivo.index('.fits')
    aorkey = nombrearchivo[71:indicefits]
    f.write(aorkey)
    f.write(';')
    for characts in carac:
        for col in columna:
            if np.any(characts == col):
                print('si')
                datoss = lectura[1].values.reshape(-1, 1).T
                f.write(str(datoss))
                f.write(';')
            else:
                print('no') 
                f.write('NA')
                f.write(';')
'''






