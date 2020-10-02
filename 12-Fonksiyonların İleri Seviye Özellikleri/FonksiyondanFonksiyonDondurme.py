# def usalma(number):
#     # two= usalma(2)
#     # three= usalma(3)
#     def inner(power):
#         return number ** power
#     return inner

# two= usalma(2)   ##   two   inner fonksiyonunu temsil ediyor 
# print(two(3))  ##    bu şekilde ekrana yazdırınca içerideki fonksiyona ulaşmış oluruz
# three=usalma(3)
# print(three(4))   #3^4 = 81


# def yetki_sorgula(page):
#     def inner(role):
#         if role=="admin":
#             return "{0}  rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0}  rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner
# admin_user=yetki_sorgula("Product Edit")

# print(admin_user("admin"))

# def islem(islem_adi):
#     def toplam(*args):
#         toplam=0
#         for i in args:
#             toplam+=i
#         return toplam
    
#     def carpim(*args):
#         carpim=1
#         for i in args:
#             carpim*=i
#         return carpim
#     if islem_adi=="toplama":
#         return toplam
#     else:
#         return carpim

# carpma=islem("toplama")
# print(carpma(10,2,2,3))