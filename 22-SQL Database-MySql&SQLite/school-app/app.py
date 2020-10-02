from dbmanager import DbManager
import datetime
from Student import Student
class App:
    def __init__(self):
        self.db = DbManager()
    
    def initApp(self):
        msg="***** \n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara göre dersler\n7-Devam Etmek istiyor musunuz?(E/Ç)"
        while True:
            print(msg)
            islem=input("Seçiminiz: ")
            if islem=="1":
                self.displayStudent()    
            elif islem=="2":
                self.addStudent()
            elif islem=="3":
                self.editStudent()
            elif islem=="4":
                self.deleteStudent()   
            elif islem=="E" or islem=="Ç":
                break
            else:
                print("*****\nYanlış Seçim!")
    
    def deleteStudent(self):
        self.displayStudent()
        studentid=int(input("ögrenci id: "))
        self.db.deleteStudent(studentid)


    def addStudent(self):
        classid=int(input("hangi sınıf: "))
        number=input("mumara ")
        name=input("ad ")
        surname=input("soyad ")
        year=int(input("yıl "))
        month=int(input("ay "))
        day=int(input("gün "))
        birthdate=datetime.date(year,month,day)
        gender=input("cinsiyet(E-K) ")

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)
    def editStudent(self):
        self.displayStudent()
        studentid=int(input("ögrenci id: "))
        student=self.db.getStudentById(studentid)
        student[0].name=input("Name: ") or student[0].name
        student[0].surname=input("Surname: ") or student[0].surname
        student[0].gender=input("Gender(E-K): ") or student[0].gender
        student[0].classid=input("Class: ") or student[0].classid
        year=input("yıl:  ") or student[0].birthdate.year
        month=input("ay: ") or student[0].birthdate.month
        day=input("gün: ") or student[0].birthdate.day
        student[0].birthdate=datetime.date(year,month,day) 
        self.db.editStudent(student[0])
       
    def displayClasses(self):
        classes=self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")
    # seçilen sınıfın öğrenci listesini ekrana yansıtır

    def displayStudent(self):
        self.displayClasses()
        classid=int(input("hangi sınıf: "))
        students=self.db.getStudentByClassId(classid)
        print("****öğrenci listesi****")
        for std in students:
            print(f"{std.id}-{std.name} {std.surname}")
        return classid
    
app=App()
app.initApp()
