x,y,z=2,5,10
numbers=1,5,7,10,6

sayi1=input("1. sayiyi giriniz")
sayi2=input("2.sayiyi giriniz")
carpim=int(sayi1)*int(sayi2)
print("sonuc:",carpim-(x+y+z))

print(y//x)
toplam=x+y+z
print(toplam%3)

x,*y,z=numbers
z**=2
print(f"z nin değeri : {z}")
ytoplam=y[0]+y[1]+y[2]
print(ytoplam)