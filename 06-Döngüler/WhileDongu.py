# # x=0
# # while x<100:
# #     print(x)
# #     x+=1

# # while x<=100:
# #     if x%2==0:
# #         print(x)
# #     x+=1


# # sayilar=[1,3,5,7,9,12,19,21]

# #1 sayilar listesini while ile ekrana yazdırın.
# # while x<len(sayilar):
# #     print(sayilar[x])
# #     x+=1

# #2 baş ve bitiş değerleri kullanıcıdan alıp aradaki tek sayıları yazdır

# # start=int(input("başlangıç değerini giriniz: "))
# # end=int(input("bitiş değerini giriniz: "))
# # while start<end:
# #     if start%2==1:
# #         print(start)
# #     start+=1

# #3 1-100 arasındaki sayıları azalan şekide yazdırın.
# # y=100
# # while y>0:
# #     print(y)
# #     y-=1

# #4 kullanıcıdan aldığınız 5 değeri ekrana yazdır

# # numbers=[]
# # hak=5
# # while hak>0:
# #     sayi=int(input("sayıyı giriniz: "))
# #     numbers.append(sayi)
# #     hak-=1

# # numbers.sort()
# # print(numbers)

# #4 kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
# #    ** ürün sayısını kullanıcıya sorun.
# #    ** dictionary listesi yapısı (name,price şeklinde olsun)
# #   --ürün ekleme işlemi bittiğinde ürünleri ekranda while sırala
    
# urunler=[]

# adet=int(input(" kaç adet ürün bilgisi gireceksiniz?"))
# i=0
# while i<adet:
#     name=input("ürünün adını giriniz:")
#     price=input("ürünün fiyatını giriniz:")
#     urunler.append(
#         {
#             'name':name,
#             'price':price
#         }
#     )


#     i+=1

# for urun in urunler:
#     print(f"ürünün adı: {urun['name']} ürününü fiyatı: {urun['price']}")

