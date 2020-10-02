import pandas as pd
import numpy as np
data=np.random.randint(10,100,15).reshape(5,3)
df=pd.DataFrame(data, index=['a','c','e','f','h'], columns=['column1','column2','column3'])

df=df.reindex(['a','b','c','d','e','f','g','h']) # reindex yapmadan önceden sorunsuz bir tablomuz var

# kendimiz karışık NaN değerlere sahip bir column oluşturuyoruz
newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df['column4']=newColumn 
# print(df)
result=df
result=df.drop('column1',axis=1) # sütun silme işlemi
result=df.drop(['column1','column2'],axis=1)
result=df.drop('a',axis=0)
result=df.drop(['a','b','d'],axis=0)
result=df.isnull() #NaN olanları False değere sahip olanları True olarak gösterir
result=df.notnull()
result=df.isnull().sum() # kolonlara göre null değerleri sayar
result=df['column1'].isnull().sum() # istediğimiz kolonun sahip olduğu null değer sayısı
result=df[df['column1'].isnull()]['column1'] #  column1 için nan değere sahip sonuçları getirir
result=df[df['column1'].notnull()]['column1']  #  column1 için nan değere sahip olmayan sonuçları getirir

result=df.dropna() # nan içeren alanları çıkarıp sayısal değerleri ekrana yazdırır ### axis=0 default değer satırı temsil eder (axis=1 sütun)
result=df.dropna(how='all') # tüm satır nan olmadığı zaman ekrana yazdırılır
result=df.dropna(how='any') # satırda 1 tane bile nan olursa yazdırılmaz default how='any' şeklindedir
result=df.dropna(subset=['column1','column2'] ,how='all') # sadece istediğimiz column için sınırlama koyabiliriz
result=df.dropna(thresh=3) # en az sayısada normal veri
result=df.fillna(value='no input') # tüm nan değerler için yeni değer atayabiliriz
result=df.fillna(value=1) 


result=df.sum() # sütunlardaki değerleri ayrı ayrı toplar
result=df.sum().sum() # tüm değerleri toplar
result=df.size # 32 tane eleman var
result=df.isnull().sum().sum() # toplam null bulunan eleman sayısı

# nan değer olan yerlere ortalama değeri yazdıran fonksiyon
def ortalama(df):   
    toplam=df.sum().sum()
    adet=df.size-df.isnull().sum().sum()
    return toplam/adet
result=df.fillna(value=ortalama(df))

print(result)