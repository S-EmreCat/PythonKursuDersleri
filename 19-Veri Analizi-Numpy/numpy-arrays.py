import numpy as np

# result=np.array([1,3,7,9])

# result=np.arange(1,10)  ## 1-9 a kadar sayılardan oluşan array oluşturur.

# result=np.arange(10,100,3) 
# result=np.zeros(10)  ## girilen değer kadar 0 dan oluşan array 
# result=np.ones(10) ## girilen değer kadar 1 den oluşan array 
# result=np.linspace(0,100,5)  ## başlangıç ve bitiş değerini eşit aralıklarla böler
# result=np.linspace(0,5,5)
# result=np.random.randint(0,10)  # 0 ile 10 arasında bir sayı üretir
# result=np.random.randint(1,10,3)  # 1-10 arasında 3 tane farklı sayı üretip array döner
# result=np.random.rand(5)  ### 0-1 arasında 5 farklı değer içeren array
# result=np.random.randn(5) ## -1 ile 1 arasında 5 farklı değer üretir

# np_array=np.arange(50)  ### 0-50 arası sayılardan oluşan dizi oluşturur
# np_multi=np_array.reshape(5,10)  ## oluşan diziyi 5 satır 10 sütun olarak şekillendirir

# print(np_multi.sum(axis=1))   ### satırlardaki sayıların toplamını verir
# print(np_multi.sum(axis=0))    ### sütunlardaki sayıların toplamını verir

rnd_numbers=np.random.randint(1,100,10)
result=rnd_numbers.max()
result=rnd_numbers.min()
result=rnd_numbers.mean()    ## dizinin ortalamasını verir
result=rnd_numbers.argmax()  ## en büyük sayının indis değerini verir
result=rnd_numbers.argmin() ## en küçük sayının indis değerini verir
print(rnd_numbers)
print(result)