from astropy.io import fits
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt

#leer tabla con los IDs que necesitan

#sacar el ID a una lista esto lo peuden hacer en pandas.
#3cambien con un editor todo lo que diga ! por ¨y usan pandas para leer el cvs.con pandas lo pasan a un dataframe y cargan solo pa primera columna.


#for id in list_of_ids
#num=id
    num=3540992
archivo='cassis_yaaar_spcfw_{}t.fits'.format(num)

print(archivo)

hdu = fits.open(archivo)
ncols = len(hdu[0].data[0,:])
wdata = np.array(hdu[0].data[:,0])
fdata = np.array(hdu[0].data[:,1])
print(hdu['data'])
#print(dir(hdu))
plt.plot(wdata,fdata)
plt.show()

#miren como se guarda una lista en un pickle y lo guardan ahi

##Preguntar a Rafael por este dato qué es y sobre HDU

#hdu = fits.open(archivo) #default is readonly
#names=tuple([hdu[0].header['COL*DEF'][x] for x,h in enumerate(hdu[0].header['COL*DEF'])])
#names+=('flag4',) #append flag4, bug in the header keywords for low-res, flag number 4 COLDEF is missing
#t=fits.BinTableHDU(data=Table(hdu[0].data, names=names), header=hdu[0].header)
#print (t)