# #************************************    range fonksiyonu     ************************

# # for item in range(7,20,2):
# #     print(item)

# # print(list(range(7,20,4)))

# #************************   enumerate fonksiyonu:::::************************************

# # normalde kelimenin harfleri hangi indexe geliyor bulma yöntemi
# # index=0
# # yazi='Hello There'
# # for letter in yazi:
# #     print(f"index:{index} harf: {letter}")
# #     index+=1

# # çıktı
# # yazi1='Hello'
# # for letter in enumerate(yazi1):     **********çıktılar arasında fark var 
# #     print(letter)

# # for index,letter in enumerate(yazi1):
# #     print(f"index:{index} harf: {letter}")


# # **********************  zip metodu  ************************
# #  -------   2 veya kaç listeyi fonk içine yazarsak index numaraları eşit olanları eşleştirerek farklı bir liste oluşturuyor
# list1=[1,2,3,4,5]
# list2=['a','b','c','d','e']
# list3=[2,5,6,8,1]
# print(list(zip(list1,list2,list3)))

# for i in zip(list2,list3):
#     print(i)
# for x,y,z in zip(list1,list2,list3):     
#     print(x,y,z)