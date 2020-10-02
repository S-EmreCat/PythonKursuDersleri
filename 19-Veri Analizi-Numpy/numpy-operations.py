import numpy as np

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)
print(numbers1)
print(numbers2)

result=numbers1+numbers2 # 2 dizinin aynı indexdeki elemanlarını toplayıp yeni dizide tutabiliyoruz
result=numbers2+10
result=numbers1 * numbers2
result=numbers1 * 10

result=np.sin(numbers1) ## trigonometrik değerlerin sonuçlarını alabiliriz
result=np.sqrt(numbers1) ## karakökünü alabiliriz
result=numbers1**2
# print(result)
mnumbers1=numbers1.reshape(2,3)
mnumbers2=numbers2.reshape(2,3)

# print(mnumbers1)
# print(mnumbers2)

# result=np.vstack((mnumbers1,mnumbers2))  ## dikey olarak ekleme yapar
# result=np.hstack((mnumbers1,mnumbers2))  ## yatay olarak ekleme yapar

result=numbers1 >=30  ## tüm elemanları kontrol edip bool değer döndüren dizi 
result=numbers2 %2==0
print(numbers2[result])  ###   koşulu sağlayan elemanları ekrana yazdırmak için

print(result)