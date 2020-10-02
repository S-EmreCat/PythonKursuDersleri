# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# kullanımı :    open(dosya_adi, dosya_erişme_modu)
# dosya erişme modu =>  dosyayı hangi amaçla açtığımızı belirtir.

########################3   "w": write  yazma modu Dosya konumda oluşturulur.  #######################3
        ### dosya içeriğini siler ve yeniden ekleme yapar. Güncellemezzz!!!!

# result=open("newfile.txt","w")    # oluşturulan dosya üzerinden işlemler yapacağımız için ona referans olsun diye resulta atarız.
# print(result)
# result.close()   # dosya açılıp işlemlerden yaptıktan sonra kaynakları tüketmesin diye kapatırız

# file1=open("C:/Users/emre_/newfile.txt","w")
# print(file1)
# file1.close()

# file2=open("newfile.txt","w",encoding='utf-8')     # utf-8 türkçe karakterleri algılar
# file2.write("Sadık Turan")
# file2.close()

######   "a"  append  ekleme. Dosya konumda oluşturulur.    Güncelleme yapar#########################3

# file2=open("newfile.txt","a",encoding='utf-8') 
# file2.write("\nswetqergheqrh")
# file2.close()

########################3   "x"  create  oluşturma.  Dosya zaten varsa hata verir.  #######################3
#file = open("newfile2.txt","x",encoding='utf-8')  # 2. kez çalışırsa var olduğu için hata verir




########################3   "r"  read   okuma.  dosya konumda yoksa hata verir.   #######################3




