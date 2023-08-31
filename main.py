from astropy.io import fits
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt


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
