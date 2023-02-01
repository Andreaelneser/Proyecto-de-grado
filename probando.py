import string
from astropy.io import fits
import glob
import pathlib
import csv 
import numpy as np
import matplotlib.pyplot as plt 
archivo_fits = "C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/cassis_yaaar_spcfw_10106112t.fits"

with fits.open(archivo_fits) as hdulist:
    #hdulist.info()
    """
    print("dir(hdulist))=",dir(hdulist))
    print("type(hdulist)=",type(hdulist))
    print(40*"*")
    print("dir(hdulist[0]))=",dir(hdulist[0]))
    print("type(hdulist[0])=",type(hdulist[0]))
    print(40*"*")
    """
    #print("hdulist[0].data =",hdulist[0].data)
    #print("type(hdulist[0].data)=",hdulist[0].data.shape)
    wdata = np.array(hdulist[0].data[:,0])
    fdata = np.array(hdulist[0].data[:,1])
    print("wdata =",wdata)
    print("fdata =",fdata)
    plt.plot(wdata,fdata)
    #plt.figure()
    #plt.plot(fdata)
    #plt.figure()
    #plt.plot(wdata)
    plt.show()
    #datoentexto = np.asarray(hdulist[0].data)
    #np.savetxt("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/cassis_yaaar_spcfw_10106112t.csv", datoentexto, delimiter=";")
    #print(40*"*")
    """
    print("hdulist[0].fileinfo() =",hdulist[0].fileinfo())
    print(40*"*")
    print("hdulist[0].header =",hdulist[0].header)
    print(40*"*")
    print("dir(hdulist[0].header) =",dir(hdulist[0].header))
    print(40*"*")
    print("hdulist[0].header.keys =",hdulist[0].header.keys)
    print(40*"*")
    print("hdulist[0].header['ProgramID'] =",hdulist[0].header['PROGID'])
    print("hdulist[0].header['AORKEY'] =",hdulist[0].header['AORKEY'])"""