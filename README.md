# Proyecto-de-grado
Clasificador de galaxias usando espectros del telescopio Spitzer para determinar si su distribución energética viene principamente de un AGN o de formación estelar.

El proyecto consiste en un proceso de ETL, limpieza, análisis y redes neuronales para la clasificación.


# Aorkey
Archivo con los ids de todos los astros que se querían analizar.

# Presentación 
En el archivo PresentacionFinal_AElneser se encuentra la presentación final del proyecto. 

# Códigos

* En el archivo "scraping.py" se encuentra el web scraping que se le hizo a la página https://irs.sirtf.com/Smart/ProgramIDs?sortcol=5;table=1;up=0#sorted_table. El objetivo de esto era obtener los aorkeys.
* En el archivo "descarga.py" se encuentra la descarga de todos los archivos FITS que corresponden con los aorkeys que se obtuvieron del web scraping. Se descargaron usando el enlace https://cassis.sirtf.com/atlas/cgi/download.py?aorkey={}&ptg={}&product=yaaar_oe_wavesamp y cambiando el aorkey dependiendo de por dónde se estuviera recorriendo la lista.
* En el archivo "recorrerparatabla.py" se extraen los datos de densidad de flujo y longitud de onda del archivo FITS en un .csv.
* En el archivo "merge.py" se hace un cruce (join o merge) entre la tabla de archivos .csv del paso anterior y otra tabla que tenía los IDs y categorías de los datos recopilados. Esto se tuvo que hacer así ya que la extracción del primer paso solo tenía los IDs, más no las categorías.
* Los demás archivos son distintas pruebas que se hicieron a lo largo del proyecto.
