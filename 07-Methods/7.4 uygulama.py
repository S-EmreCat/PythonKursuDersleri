#1 

# def writetheword(word='boş',number=1):
#     while number > 0:
#         print(word)
#         number-=1

# writetheword('emre',5)

# #2
# def listele(*sayilar):
#     liste=[]
#     liste.append(sayilar)
#     print(liste)
    
# listele(2,38,96,63,53)

# 3
# def asalsayi(a,b):
    
#     for i in range(a,b+1):
#         if i>1:
#             for y in range(2,i):
#                 if (i % y ==0):
#                     break
#             else:
#                 print(i)
# asalsayi(4,13)

#4 
def tambolen(sayi):
    liste=[]
    
    for i in range (2,sayi+1):
        if sayi%i==0:
            liste.append(i)
    print(liste)

tambolen(27)

        