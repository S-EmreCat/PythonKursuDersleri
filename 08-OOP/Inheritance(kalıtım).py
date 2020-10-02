
class Person():
    def __init__(self,fname,lname):
        self.ad=fname
        self.soyad=lname
        print("Person Created")
    def who_am_i(self):
        print('I am a Person')


class Student(Person):
    def __init__(self,dene1,dene2,number): 
        Person.__init__(self,dene1,dene2)    ##### Person class ınıın initinni ezmemek için bunu yazıyoruz

        self.stuNumber=number
        print("Student Created.")
    
    #############    override     aynı isimli method temel sınıftaki methodu ezer
    def who_am_i(self):
        print('I am a Student')



p1=Person('Emre','Çat')

p2=Student('Enes','sadfhg',1256)

print(p1.ad,p1.soyad)
print(p2.ad,p2.soyad, p2.stuNumber)

p1.who_am_i()
p2.who_am_i()