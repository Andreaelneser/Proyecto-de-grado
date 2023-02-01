import wget
import time
import random

with open("C:/Users/HABI/Documents/Universidad/CODIGOTESIS/AorkeyM1.txt") as f:
    lines = f.readlines() #Se lee el archivo aorkey.txt y se guarda en una lista

for line in lines: #Recorre la lista lines
    for ptg in range(1, 118): #Se recorre el rango de 1 a 119
        ptg = str(ptg) #Se convierte el numero a string
        without = line.replace("\n", "") #Se quita el salto de linea
        print(without, ptg) #Se imprime el nombre del aorkey y el numero de ptg
        try:    
            #time.sleep(10 + random.randint(0, 120))
            wget.download("https://cassis.sirtf.com/atlas/cgi/download.py?aorkey={}&ptg={}&product=yaaar_oe_wavesamp".format(
                without, ptg), 'C:/Users/HABI/Documents/Universidad/CODIGOTESIS/Descarga') #Se descarga el archivo reemplazando lo del for
            print("Descarga 1 exitosa") 
        except Exception as e: #Se imprime el error
            try :
                wget.download("https://cassis.sirtf.com/atlas/cgi/download.py?aorkey={}&ptg=0&product=yaaar_oe_wavesamp".format(
                without), 'C:/Users/HABI/Documents/Universidad/CODIGOTESIS/Descarga')
                print("Descarga 2 exitosa") 
            except Exception as e1:
                print("Decarga 2 fallida:", e1)
                break
            print("Decarga 1 fallida:", e)
            break 



