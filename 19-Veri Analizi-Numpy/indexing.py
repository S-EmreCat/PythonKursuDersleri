import numpy as np

numbers=np.array([0,5,10,15,20,25,50,75])

result=numbers[5]  ## direkt index numarasına ulaşabiliriz
result=numbers[0:3]  # ilk 3 eleman
result=numbers[3:]   # 3. elemandan sona kadar
result=numbers[::]   # tüm liste
result=numbers[::-1]   # listeyi ters çevirir


numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])

result=numbers2[2]  # >> [50,75,85] çıktısı alınır  # 2. indexindeki satırı getirir

result=numbers2[0,2] ## >> 10 çıktısını verir 1. satır 3. sütun
result=numbers2[:,2] ## : tüm satırları seçer, 2. indexli elemanlar >> [10,25,85]
result=numbers2[:,0:2]
result=numbers2[-1,:]  ## -1 yani son satır ın tüm sütunlarını al

# print(result)

arr1=np.arange(0,10)
#arr2=arr1 # referans
# arr2[0]=20  ## aynı bellekte tutuldukları için arr1 de 0. index 20 olur

arr2=arr1.copy() # kopya işlemi yaparsak farklı bellek kullanılır 
arr2[0]=20       ## sadeece arr2 değişir
print(arr1)

print(arr2)