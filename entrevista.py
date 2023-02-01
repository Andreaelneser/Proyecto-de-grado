import pandas as pd
import numpy as np
import csv

#call two csv files
df2 = pd.read_csv('https://recruitment.dev.frubana.com/api/queries/142/results.csv?api_key=qPPQjb7kOTEfQPNTGpKOzwBBx8OCReeYSatvNYKr') #purcharse orders
df1 = pd.read_csv('https://recruitment.dev.frubana.com/api/queries/144/results.csv?api_key=p0ibcUb3T2pq3cVrufMyXhjQYyszYkWuz32KkOz1')  #products 

#print(df1.head())
#print(df2.head())

#merge two csv files
df3 = pd.merge(df1, df2, left_on=['id'], right_on=['product_id'], how='inner')
print(df3.head())

df4= df3.groupby(['id_x','name']).sum()
print(df4.head())

