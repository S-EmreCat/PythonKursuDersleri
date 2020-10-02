# # class

# class Person:
#     #pass  # içi bir bir class oluşturup hata almamak için içines pass yazıyoruz
#     # class attributes 

#     address='no information'


#     #constructor (yapıcı method)
    
#     def __init__(self, name, year):   # self p1,p2 gibi classtan türetilen nesneleri temsil eder
#         #object attributes              # init fonksiyonu p1,p2 gibi nesneler çalıştırıldığı anda çalışıyor 
#         self.name=name
#         self.birthyear=year

#     # instance method
#     def intro(self):
#         print(f" Hello  There. I am "+self.name)

#     def calculateAge(self):
#         return 2020-self.birthyear

# #objecti (instance)
# p1=Person(name="Emre", year=1997)  # bu şekilde yazmamız bile initin çalışması için yeterli
# p2=Person("Enes",2003)              # 2 şekilde de nesneyi tanımlayabilirz

# p1.intro()
# p2.intro()

# print(f" yaşım: {p1.calculateAge()}")
# print(f" yaşım: {p2.calculateAge()}  adım: {p2.name}")



# #updating
# # p1.name='Ahmet'
# # p1.address='Bursa'

# # #  accessing object attributes
# # print(f'name: {p1.name} year: {p1.birthyear} address: {p1.address}')
# # print(f'name: {p2.name} year: {p2.birthyear} address: {p2.address}')




###############################################################################################################


class Circle:
    #Class attribute
    pi=3.14
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
        
    #methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1=Circle() # yaricap=1
c2=Circle(5)

print(f" c1 alan : {c1.alan_hesapla()} c1 cevre:: {c1.cevre_hesapla()} ")
print(f" c2 alan : {c2.alan_hesapla()} c2 cevre: {c2.cevre_hesapla()}")