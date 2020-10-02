import pandas as pd
import numpy as np

data=[['Ahmet',50],['Ali',60],['Yağmur',70],['Çınar',80]]
dict={'name':['Ahmet','Ali','Yağmur','Çınar'],'Grade':[50,60,70,80]}
dict_list=[
    {"Name":"Ahmet",'Grade':50},
    {"Name":"Ali",'Grade':60},
    {"Name":"Yağmur",'Grade':70},
    {"Name":"Çınar",'Grade':80}
]
# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame([['Ahmet',50],['Ali',60],['Yağmur',70],['Çınar',80]]) # şeklinde çağırırsak sütun isimlerini 0-1-2 şeklinde sıralar
# df=pd.DataFrame(data,columns=['Name','Grade'],index=[10,22,33,41])  # bu şekilde datayı dışarıdan gönderim sütunlara isim verebiliriz istediğimiz index numarasını atayabiliriz.
# df=pd.DataFrame(dict)  ## DataFrame olarak dictionary gönderirsek tüm bilgileri içerisinde verebiliriz.
df=pd.DataFrame(dict_list,index=['201','401','123','523']) # istersen tekrar index düzenlemesi yapabiliriz.
print(df)




# s1=pd.Series([3,2,0,1])
# s2=pd.Series([0,3,7,2])
# data=dict(apples=s1,oranges=s2)
# df=pd.DataFrame(data)
# print(df)
"""  çıktımız
   apples  oranges
0       3        0
1       2        3
2       0        7
3       1        2
"""