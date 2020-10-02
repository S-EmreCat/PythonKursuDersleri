# girilen sayı asal mı değil mi

sayi=int(input("sayi gir"))
asalmi=True

if sayi==1:
    asalmi=False
for i in range(2,sayi):
    if sayi%i==0:
        
        asalmi=False
        break

if asalmi:
    print("sayi asal")
else:
    print("sayi asal değil")
    