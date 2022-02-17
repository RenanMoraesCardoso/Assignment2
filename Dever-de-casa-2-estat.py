# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_excel(r"C:/Users/renan/OneDrive/Documentos/Economia/BL2013_MF2599_v2.2.xls", sheet_name="Sheet1")
print(df.head(10))

df2 = pd.read_excel("C:/Users/renan/OneDrive/Documentos/Economia/BL2013_MF2599_v2.2.xls", sheet_name="Sheet1", header=1152)
print(df2.head(10))

df3 = df2.iloc[0:13,11]

print(df3)

df4 = pd.Series([1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010])

df5 = pd.concat([df4,df3], axis=1).rename(columns={0:"Ano",'Unnamed: 11':'Escolaridade média'})
print(df5)
Grafico1 = df5.plot.line(x='Ano',y='Escolaridade média')

serie = pd.Series({'Sem escolaridade':12.4, 'Primário':37,'Secundário':39.3,'Terciário':11.3}, name = '% da população com 25 anos ou mais que alcançaram determinada escolaridade')
print(serie)
serie.plot.pie()
