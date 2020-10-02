import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
df=pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result=df
result=df.columns  # DataFrame'in column isimlerine ulaşmak için
result=df.head(5) # ilk 5 satırı almak için
result=df.head(10)
result=df.tail(5) # son 5 satırı almak için
result=df["Column1"].head(5)  ## Column1 in ilk 5 satırı
result=df.Column1.head(5)   ## Column1 in ilk 5 satırı
result=df[["Column1","Column2"]].tail(5)  # birden fazla column için 
result=df[5:15][["Column1","Column2"]].tail(5)  ### 5-15. satırlar arasından istediğimiz column için bilgi alabiliriz
result=df[5:15][["Column1","Column2"]].head(5)

##  filtreleme yapma

result=df[df>50]  # koşul için arama yapmak istersek
result=df[df%2==0] # tüm df üzerinden koşul arattık
result=df["Column1"]>50  # Column1 için kontrol
result=df[df[["Column1","Column2"]]>50][["Column1","Column2"]]  ##  İstediğimiz Column için İstediğimiz koşula bağlı sonuca ulaşma
result=df[ (df["Column1"]>50)  & (df["Column2"]<=70)]
result=df[ (df["Column1"]>50)  | (df["Column2"]<=70)][["Column1","Column2"]]
result=df.query("Column1 >= 50 & Column2 %2==0")[["Column1","Column2"]]  # query fonksiyonu ile de koşul kontrolü yapılabilir

print(result)

