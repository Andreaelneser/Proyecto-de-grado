import pandas as pd
import numpy as np


df = pd.read_csv("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/TablaSoloImportantes.csv", sep=';')

df1 = df.iloc[:,0:360]

for columna in df1:
    for fila in df1:
        #convert to float
        df1[columna] = df1[columna].astype(float)


    #df1[columna].fillna(df1[columna.median], inplace=True)

