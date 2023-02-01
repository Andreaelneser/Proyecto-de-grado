from unicodedata import category
from bs4 import BeautifulSoup
import requests 
import csv 

url = "https://irs.sirtf.com/Smart/ProgramIDs?sortcol=5;table=1;up=0#sorted_table"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', class_='foswikiTable')

with open('C:/Users/HABI/Documents/Universidad/CODIGOTESIS/programs.csv', 'a') as programs:
    programs.write("ProgramID"+";"+"Category\n")
for ProgramID in table.find_all('tbody'):
    rows = ProgramID.find_all('tr')
    for row in rows:    
        program_ids = row.find('td', class_='foswikiTableCol1')
        print (program_ids.text)
        categorys = row.find('td', class_='foswikiTableCol3')
        print (categorys.text)

        with open('C:/Users/HABI/Documents/Universidad/CODIGOTESIS/programs.csv', 'a') as programs:
            programs.write(program_ids.text+";"+categorys.text+"\n")

        