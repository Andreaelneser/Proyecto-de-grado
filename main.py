#import wget
import time
import random

with open('aorkey.txt') as f:
    lines = f.readlines()

urls = []

for line in lines:
    without = line.replace("\n", "")
    #time.sleep(60+random.randint(0, 120))
    #urls.append("https://cassis.sirtf.com/atlas/cgi/download.py?aorkey={}&ptg=0&product=yaaar_oe_wavesamp".format(without))

for x in range(0, len(urls)):
    wget.download(urls[x], 'C:/Users/hp/Downloads/Archivos')
    print(x)
