# def square(num): return num ** 2
# numbers=[1,3,5,9]
# result=list(map(square,numbers))

# #veya
# for item in map(square,numbers):
#     print(item)
# print(result)


# # lamda methodu kullanımı *******   square fonk her zaman kullanmayız kısa bir şey lazımsa bu şekilde yaparız ::::::

# sayilar=[2,4,6,8]
# sonuc= list(map(lambda num: num**2,numbers))
# print(sonuc)

# # veya 
# for i in map(lambda param: param**3,numbers):
#     print(i)

######    lamda ile basit fonk yazma  #############

# karealma=lambda sayi: sayi**2
# sonuc=karealma(3)
# print(sonuc)


##### Lambda da filter yapma ####

numbers=[2,5,7,22,16,25]
def chech_even(num): return num%2==0

sonuc1=list(filter(chech_even,numbers))
sonuc2=list(filter(lambda num: num%2==0,numbers))    # lamda ile yapıımı
print(sonuc1,sonuc2)