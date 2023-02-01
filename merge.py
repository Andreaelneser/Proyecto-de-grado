import pandas as pd
import numpy as np
import csv

#call two csv files
df2 = pd.read_csv('C:/Users/HABI/Documents/Universidad/CODIGOTESIS/programs.csv', sep=';')
df1 = pd.read_csv('C:/Users/HABI/Documents/Universidad/CODIGOTESIS/programsfromaorkeys.csv', sep=';')

print(df1.head())
print(df2.head())

#merge two csv files
df3 = pd.merge(df1, df2, on=['ProgramID'], how='outer')

with open('C:/Users/HABI/Documents/Universidad/CODIGOTESIS/unionTotales.csv', 'a') as union:
    union.write("ProgramID"+";"+"Aorkey"+";"+"Category\n")
    for index, row in df3.iterrows():
        union.write(str(row['ProgramID'])+";"+str(row['Aorkey'])+";"+str(row['Category'])+"\n")
    union.close()


