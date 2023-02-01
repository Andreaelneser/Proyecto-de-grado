import string
from astropy.io import fits
import glob
import pathlib
carpetaARecorrer="C:/Users/HABI/Documents/Universidad/CODIGOTESIS/CopiaDeDescar/"

archivos=list(pathlib.Path(carpetaARecorrer).glob('*.fits'))
archivos.sort()
print(len(archivos))
with open ("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/programsfromaorkeys.csv", 'w') as programsfromaorkeys:
    programsfromaorkeys.write("ProgramID"+";"+"Aorkey\n")
    for archivo_fits in archivos:
        #archivo_fits=archivos[0]
        print(archivo_fits)
        try:
            with fits.open(archivo_fits) as hdulist:
                #hdulist.info()
                print("hdulist[0].header['ProgramID'] =",hdulist[0].header['PROGID'])
                print("hdulist[0].header['AORKEY'] =",hdulist[0].header['AORKEY'])
                programsfromaorkeys.write(str(hdulist[0].header['PROGID'])+";"+str(hdulist[0].header['AORKEY'])+"\n")
        except Exception as e:
            print(e)
    programsfromaorkeys.close()
    







