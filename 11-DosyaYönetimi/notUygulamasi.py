def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')
    ogrenciAdi=liste[0]
    notlar=liste[1].split(",")
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not1+not2+not3)/3
    if ortalama>90:
        harf="AA"
    elif ortalama>85 and ortalama<=90:
        harf="BA"
    elif ortalama<85 and ortalama>70:
        harf="CC"
    elif ortalama<71 and ortalama>50:
        harf="CC"
    else:
        harf="FF"
    return ogrenciAdi + ": "+harf + "\n"

def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad=input("Öğrenci adı: ")
    soyad=input("Öğrenci soyadı: ")
    not1=input("not1 adı: ")
    not2=input("not2 adı: ")
    not3=input("not3 adı: ")
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+" : "+ not1+","+not2+","+not3+"\n")
        

def notlari_kayıtet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
while True:
    islem=input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış")
    if islem=='1':
        ortalamalari_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        notlari_kayıtet()
    else:
        break