import pandas as pd
import numpy as np

data={
    'Column1':[1,2,3,4,5],
    'Column2':[10,20,13,45,25],
    'Column3':["abc","bca","ade","cba","dea"]
}

df=pd.DataFrame(data)

result=df
result=df['Column2'].unique() # tekrarlamayan bilgileri gösterir
result=df['Column2'].nunique() # kaç tane farklı değer var sayısını verir
result=df['Column2'].value_counts() # hangi elemandan kaç tane var sayısını verir
result=df['Column2']*2 # matematiksel işlemler yapabiliriz

def kareal(x):
    return x*x
kareal2=lambda x: x*x
result=df['Column1'].apply(kareal) # bir sütuna fonksiyonu bu şekilde gönderip çıktı alıyoruz   apply fonksiyonu ile
result=df['Column1'].apply(kareal2)
result=df['Column1'].apply(lambda x: x*x) # apply fonka direk işlem gönderebiliriz
result=df['Column3'].apply(len) # str değerler için len fonk u direkt gösterebliiriz apply içerisine
df['uzunlukları']=df['Column3'].apply(len) # yeni bir sütun yapmak içinde kullanabiliriz
result=df.columns
result=len(df.columns)
result=len(df.index)
result=df.info
result=df.sort_values("Column2") # Column2 küçükten büyüğe sıralanır
result=df.sort_values("Column2",ascending=False)    # Column2 büyükten küçüğe sıralanır
# result=df.sort_values("Column3") #Column3 alfabetik sıralanır

# print(df) 
print(result)