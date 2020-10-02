import pandas as pd

from numpy.random import randn

df =pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])

result=df
result=df['Column1']
result=df[['Column1','Column2']] ## birden fazla column istersek liste şeklinde göndermemiz gerekir

# loc kullanımı 
# loc["row","column"] ----  loc["row"] ---- loc[":","column"]
result=df.loc['A'] ## A satırındaki değerleri almak istersek 
result=df.iloc[2]  ## 0-1-2 gibi indexlerle çalışmak istersen iloc kullanıyoruz
# result=type(df.loc['A']) # pandas.series
# result=df.loc[:,'Column1']
# result=df.loc[:,['Column1','Column2']] ## seçili column sonuçlarını istersek
# result=df.loc[:,'Column1':'Column3']  ## birden fazla column seçimi yapmak istersek
# result=df.loc[:,:'Column3'] # başlangıçtan istenilen yere kadar
# result=df.loc["A":"B",:'Column2'] # aynı işlemleri satır içinde yapabiliyoruz
# result=df.loc["A","Column2"]  # istediğimiz değeri almak için satır sütun olarak girdi-çıktı ilişkisi kurabiliriz.

df["Column4"]=pd.Series(randn(3),["A","B","C"])  ### column eklemek için 
df["Column5"]=df["Column2"]+df["Column3"]  ### 2 columnun toplamını yeni columnda göstermek

print(df.drop("Column5",axis=1))
print(df)
# print(result)

