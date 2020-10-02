# def cube(): 
#     result=[]      ### liste hafızada fazladan yer kaplıyor ama bizim istediğimiz sadece ekrana yazdırmak liste olmasa da olur 
#     for i in range(5):
#         result.append(i**3)
#     return result
# print(cube())

# def cube1():
#     for i in range(7):
#         yield i**3   #### yield ile fonksiyon döndürünce bellekte bir yer kaplamıyor çoklu verilerde işe yarıyor

# for i in cube1():
#     print(i)

# iterator=cube1()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# liste=[i**3 for i in range(5)]    [] ile belirtince hafızada yer kaplayan bir liste oluşturuyoruz

generator=(i**3 for i in range(5))     #  () ile yazarsak gelen sonucu generator olarak döndürürüz
print(generator)

# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in generator:
    print(i)