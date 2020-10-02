import mysql.connector 
import datetime
from connection import connection

class Student:
    connection=connection
    mycursor=connection.cursor()
    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id=0
        else:
            self.id=id
        self.studentNumber=studentNumber
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.gender=gender
        

    def saveStudent(self):
        sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) Values (%s,%s,%s,%s,%s)"
        value=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
            print(f"son eklenen kaydın id numarası: {Student.mycursor.lastrowid}")
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            Student.connection.close() # bağlantıyı kapatmamız lazım
            print("database bağlantısı kapandı.")
            
    @staticmethod
    def saveStudents(students):
        sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) Values (%s,%s,%s,%s,%s)"
        values=students
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
            print(f"son eklenen kaydın id numarası: {Student.mycursor.lastrowid}")
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            Student.connection.close() # bağlantıyı kapatmamız lazım
            print("database bağlantısı kapandı.")
    
    # 22.17 UYGULAMA
    @staticmethod
    def StudentInfo():
        #   a- Tüm öğrenci kayıtlarını alınız.
        sql="SELECT * FROM student"
        #   b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
        sql="SELECT StudentNumber,Name,Surname FROM student"
        #   c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
        sql="SELECT * FROM student where Gender='K'"
        #   d- 2003 doğumlu öğrenci bilgilerini alınız. 
        sql="SELECT * FROM student where YEAR(Birthdate)=2003"
        #   e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
        sql="SELECT * FROM student where YEAR(Birthdate)=2005 and name='Ali'"
        #   f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
        sql="SELECT * FROM student where Name LIKE '%an%' or Surname LIKE '%an%'"
        #   g- Kaç erkek öğrenci vardır ?
        sql="SELECT Count(*) FROM student where Gender='E'"
        #   h- Kız öğrencileri harf sırasına göre getiriniz.
        sql="SELECT * FROM student where Gender='K' Order By name" 
        

        Student.mycursor.execute(sql)
        try:
            results = Student.mycursor.fetchall()
            for result in results:
                print(f'{result}')
        except mysql.connector.Error as err:
            print('hata: ',err)
        finally:
            Student.connection.close() # bağlantıyı kapatmamız lazım
            print("database bağlantısı kapandı.")

    @staticmethod
    def getStudentById(id):
        sql="Select * from student where id=%s"
        value=(id,)
        Student.mycursor.execute(sql,value)
        try:
            return Student.mycursor.fetchone()
        except mysql.connector.Error as err:
            print("Error: ",err)
       


# 5- Aşağıdaki güncelleme sorularını yapınız.
#   a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

     # UPDATE STUDENT FON
    def updateStudent(self):
        sql="UPDATE student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s where id=%s"
        values=(self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Error: ",err)
       


obje=Student.getStudentById(6)
student=Student(obje[0],obje[1],obje[2],obje[3],obje[4],obje[5])
student.name='Emre'
student.surname='Çat'
student.updateStudent()
# Student.StudentInfo()

# ahmet=Student("552","Ahmet","Yılar",datetime.datetime(2005,5,17),"E")
# ahmet.saveStudent()

# öğrenciler=[
#     ("301","Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E"),
#     ("302","Ali","Can",datetime.datetime(2005,6,17),"E"),
#     ("303","Canan","Tan",datetime.datetime(2005,7,17),"K"),
#     ("304","Ayşe","Taner",datetime.datetime(2005,9,23),"K"),
#     ("305","Bahadır","Toksöz",datetime.datetime(2004,7,17),"E"),
#     ("306","Ali","Cent",datetime.datetime(2003,8,17),"E"),
# ]
# Student.saveStudents(öğrenciler)




