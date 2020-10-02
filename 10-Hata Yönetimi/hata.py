# error => hata
# error handling => hata yönetimi


# try:                      #####     hatanınbeklendiği kısım try içine yazılır
#     x=int(input('x:'))
#     y=int(input('y:'))
#     print(x/y)
# except ZeroDivisionError:          #####   hata sonucunda yapılacak işlemler except içine yazılır
#     print("y için 0 girilemez")
# except ValueError:
#     print("x ve ye için sayı gir")

# except (ZeroDivisionError,ValueError)  as e :   #####    çoklu hataları bu şeklide tespit ediyoruz
#     print("yanlış bilgigirdiniz")
#     print(e)                          #####    parantez içindeki hangi hatayı yakaladıysa as ile isimlendirip böyle öğreniriz
# else:
#     print(" her şey yolunda")          #### hatasızz çalıştığı zaman çıktı istiyorsak except çalışmazsa else çalışır

# while True:                            ### bu şekilde doğru bilgi girilene kadar döngü oluşturulup try kullanımı yapılır
#     try:
#         a=int(input('a:'))
#         b=int(input('b:'))
#         print(a/b)
#     except Exception as ex:              #### exception hataların geneller bilgi verir
#         print("yanlış bilgi girdiniz",ex)
#     else:
#         break 
#     finally:          ##### her koşulda çalışır    dosya okuma işlemi yapılırken dosyayı kapatmak gibi amaçlarda kullanılır
#         print("try except sonlandı")
