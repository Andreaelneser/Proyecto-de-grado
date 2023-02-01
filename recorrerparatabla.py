import string
from astropy.io import fits
import glob
import numpy as np
import matplotlib.pyplot as plt 
import csv

columna0 = []
path = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar"


for filename in glob.glob(path + "/*.fits"):
    with fits.open(filename) as hdulist:
        wdata = np.array(hdulist[0].data[:,0])  #wavelength
        fdata = np.array(hdulist[0].data[:,1]) #flux
        columna0 = [*columna0, *wdata]

        columna0 = list(set(columna0))
        columna0.sort()
        
f= open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/TablaConTodos.csv","w") 
wr = csv.writer(f, quoting=csv.QUOTE_NONE, delimiter=";")
wr.writerow(['{:1.18e}'.format(x) for x in columna0]+['Aorkey']+['Etiqueta'])
f.close()


for filename in sorted(glob.glob(path + "/*.fits")):
    with fits.open(filename) as hdulist:
        nombrearchivo = str(filename)
        indicefits = nombrearchivo.index('.fits')
        aorkey = nombrearchivo[81:indicefits]

        wdata = np.array(hdulist[0].data[:,0])
        fdata = np.array(hdulist[0].data[:,1])

        fila = np.array([])
        f= open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/DatosCSV/TablaConTodos.csv","a") 

        for i in range(0, len(columna0)):
            bandera = 0
            for j in range(0, len   (wdata)):
                if columna0[i] == wdata[j]:
                    f.write("{:1.18e}".format(fdata[j]))
                    f.write(';')
                    bandera = 1 
                    break 
            if bandera == 0:
                f.write('NaN')
                f.write(';')
        f.write(aorkey)
        f.write('\n')
        f.close()


