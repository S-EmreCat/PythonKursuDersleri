import pandas as pd
import numpy as np

data=pd.read_csv("nba.csv")
#1
result=data
# print(result.head(10))
#2 toplam kayıt sayısı
# print(len(data.index)) >> 458
# print(result['Name'].count()) # >> 457
#3 Tüm oyuncuların toplam maaş ortalaması:
# maaş=data['Salary'].mean() # 4842684.105381166
# print(maaş)
#4 en yüksek maaş
# print(data['Salary'].max()) #25000000.0
#5 en yüksek maaşı olan oyuncu  (kendim yapamadım)
# result=data[data['Salary']==data['Salary'].max()]['Name'].iloc[0]  ## 
# print(result)

#6 yaşı 20-25 arasında olan oyunların ismi ve takımları 113 sonuç
# yaş=data[(data['Age']<25) & (data['Age']>20)]
# print(yaş[['Name','Team','Age']].sort_values('Age')) 
#7 John Holland isimli oyuncunun oynadığı takım?
# isim=data[data['Name']=='John Holland']
# print(isim['Team'].iloc[0])

#8 takımlara göre maaş ortaması
# print(data.groupby('Team')['Salary'].mean())
#9 kaç farklı takım var
# print(data['Team'].nunique()) #30
#10 her takımda kaç oyuncu oynamaktadır
# takımlar=data.groupby('Team')['Name'].count()
# print(takımlar)

# adında "and" geçen takımları bul
## 1. yöntem
# data.dropna(inplace=True)
# def str_find(name):
#     if "and" in name.lower():
#         return True
#     return False
# result=data[data['Name'].apply(str_find)]


## 2. yöntem
df=data.dropna() # nan ifade bulunanları çıkarttık
result=df[df['Name'].str.contains('and')]
print(result)
