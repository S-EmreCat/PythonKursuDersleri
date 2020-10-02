# liste =["1","2","5a","10b","abc","50","10"]

# # liste elemanları içindeki sayısal değerleri bulunuz.

# for i in liste:
#     if i.isdigit():
#         print(f"girdiğiniz değer sayısal  {i} ")

        
# for x in liste:
#     try:
#         result=int(x)
#         print(result)
#     except ValueError:
#         continue





#kullanıcı q değerini girmedikce aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata
# mesajı yazınız.

# while True:
#     x=input("sayı giriniz...")
#     if x=='q':
#         print("q girildi program kapanıyor.")
#         break
#     try:
#         result=float(x)
#         print("girdiğiniz sayi: ",result)
#     except ValueError:
#         print("geçersiz değer")


# girilen parola içinde türkçe karakter hatası veriniz.

# import re
# def checkPass(passw):
#     if re.search("[ğüıİşç]",passw):
#         raise Exception("parola türkçe karakter içeriyor")
    
# parola=input("şifrenizi giriniz.")
# try:
#     checkPass(parola)
# except TypeError as err:
    # print(err)

# faktöriyel fonksiyonu oluşturup fonksiyona 
# gelen değer için hata mesajları verin

# def factoriyel(sayi):
    
#     sonuc=1
#     if sayi<=0:
#             raise Exception("0 dan büyük sayi giriniz")
#     else:
#         for i in range(1,sayi+1):
#             sonuc*=i
#             print("sonuc: ", sonuc)

# try:
#     sayi1=int(input("sayı giriniz"))
#     factoriyel(sayi1)
# except ValueError:
#     print("Yanlış değer girdin sayi gir")
    



    