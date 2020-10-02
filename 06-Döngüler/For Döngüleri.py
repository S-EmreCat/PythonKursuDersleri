# name = 'Emre Çat'
# for i in name:
#     print(i)

# 62 for döngü uygulama
sayilar=[1,3,5,7,9,12,19,21]
# #1. soru
# 
# for i in sayilar:
#     if i%3==0:
#         print(i)

#2. soru
# toplam=0
# for i in sayilar:
#     toplam+=i
# print(toplam)    
ürünler=[
    {'name':'samsung s6','price': '3000'},
    {'name':'samsung s7','price': '4000'},
    {'name':'samsung s8','price': '5000'},
    {'name':'samsung s9','price': '6000'},
    {'name':'samsung s10','price': '7000'},
]
#5  ürünlerin toplam fiyatı
# toplam=0
# for urun in ürünler:
#     toplam+=int(urun['price'])
# print(toplam)

#6 5000den az ücretli ürünler
for urun in ürünler:
    fiyat=int(urun['price'])
    if fiyat<=5000:
        print(f'bu ürünün fiyatı 5000den az {urun["name"]}')