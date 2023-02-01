import string
from astropy.io import fits
import glob
import numpy as np
import matplotlib.pyplot as plt 

#recorrer carpeta
path = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar"
for filename in glob.glob(path + "/*.fits"):
    print(filename)
    with fits.open(filename) as hdulist:
        print("hdulist[0].data =",hdulist[0].data)
        print("type(hdulist[0].data)=",hdulist[0].data.shape)
        wdata = np.array(hdulist[0].data[:,0])
        fdata = np.array(hdulist[0].data[:,1])
        plt.plot(wdata,fdata)
        #save image
        plt.savefig("{}.jpg".format(filename))
        plt.close()
        datoentexto = np.asarray(hdulist[0].data)
        np.savetxt("{}.csv".format(filename), datoentexto, delimiter=";")
        