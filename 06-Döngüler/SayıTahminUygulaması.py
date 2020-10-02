# '''
#     1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
#         ** random modüşü için arama yapın.
#         //100 üzerinden puanlama yapın her soru 20 puan
#         ***  hak bilgisini kullanıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın
# '''
# import random
# hak=5
# sayac=0
# sayi=random.randint(1,3)



# name=input("lütfen yarışma adınızı giriniz.")
# while hak>0 :
#     hak-=1
#     sayac+=1
#     tahminsayisi=int(input("tahmin ettiğiniz sayiyi giriniz:"))
#     if tahminsayisi<sayi:
#         print("yukarı çık...")
        
#     elif tahminsayisi>sayi:
#         print("aşşağı in...")
        
#     elif tahminsayisi==sayi:
#         print(f"doğru sayıyı buldunuz puanınız: {100-((5-hak)*20)} Tebrikler. {sayac}. defada bildiniz")
#         break
        
#     if hak==0:
#         print("sayıyı bulamadınız. Hakkınız bitti Puanınız 0 ")
    