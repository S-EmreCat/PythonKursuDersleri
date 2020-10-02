import pandas as pd
import numpy as np

# numpy gibi dizideki tüm elemanlar aynı tür olmak zorunda değil
#data
# numbers=[20,30,40,50]
# letters=['a','b','v',3]
# scalar=122
# dict={'a':10,'b':20,'c':30,'d':40}
# random_number=np.random.randint(10,100,6)


# pandas_series=pd.Series()
# pandas_series=pd.Series(numbers)
# pandas_series=pd.Series(letters)
# pandas_series=pd.Series(scalar)
# pandas_series=pd.Series(5,[0,1,2,3,4,5])  ### 0-5 indexlerine 5 i yerleştirip dizi oluşturur
# pandas_series=pd.Series(numbers,['a','b','c','d'])  ## index olarak a-b-c-d yi tutuyoruz eleman sayıları eşit olması
# pandas_series=pd.Series(dict)  # key bilgilerini index olarak tutar
# pandas_series=pd.Series(random_number)  ## numpy kullanarak ürettiğimiz dizi elemanlarını pandas içine atabiliriz

# pandas_series=pd.Series([20,30,40,50],['a','b','c','d']) # 0. indexi çağırırsak 20 bilgisine ulaşırız
# result=pandas_series[0] # 20
# result=pandas_series[-1] # 50
# result=pandas_series[:2]
# result=pandas_series['a']  # kendimiz 0. indexe a harfini atadığımız için bu şekilde de 20 de ğerine ulaşabiliriz
# result=pandas_series[['a','c']] ### birden fazla bilgiye ulaşmak istersek tekrar [] içerisinde çağırırız
# result=pandas_series.sum() ## numpy da olduğu gibi sum shape ndi max min fonksiyonlarını kullanabiliriz
# result=pandas_series+50  # matematiksel işlemler yapabiliriz
# result=pandas_series >= 50 # kontrol işlemleri yapılabilir
# result=pandas_series %2==0
# print(pandas_series[pandas_series %2==0])  ## true false yerine direkt sayıları istiyorsak bu şekilde sonuç alabiliriz
# print(pandas_series)
# print(result)


opel2018=pd.Series([20,30,40,50],["astra","corsa","mokka","insignia"])
opel2019=pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])
total=opel2018+opel2019  ####   Grandlan ve mokka için 2 tabloda ortak değer olmadığı için NaN değeri dönüyor

print(total)
print(total['astra']) # direkt olarak astranın 60 değerini ekrana yazdırır