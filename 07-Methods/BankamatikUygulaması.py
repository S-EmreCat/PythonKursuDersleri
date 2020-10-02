hesapA={
    'ad': 'Sadık Turan',
    'hesapNo': '1235774',
    'bakiye': 3000,
    'ekhesap': 2000
}
hesapB={
    'ad': 'Ali Turan',
    'hesapNo': '1242774',
    'bakiye': 2000,
    'ekhesap': 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye']>=miktar:
        hesap['bakiye']-=miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam=hesap['bakiye']+hesap['ekhesap']
        if toplam>=miktar:
            ekHesapKullanimi=input(" ek hesap kullanılsın mı? (e/h)...\n")
            if ekHesapKullanimi=='e':
                print('paranizi alabilirsiniz')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
        else:
            print("üzgünüz bakiye yetersiz")


paraCek(hesapA,3000)

paraCek(hesapA,1000)