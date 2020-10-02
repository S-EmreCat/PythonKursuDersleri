import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
from mysql.connector.locales.eng import client_error


class DbManager:
    def __init__(self):
        self.connection=connection
        self.cursor=self.connection.cursor()
## Student nesnesinden göndermemiz uygun şartlardan geçip hata vermeyecek bir bilgi gönderdiğimizi kontrol etmemizi sağlar
    def getStudentById(self,id):  
        sql="Select * from student where id =%s"
        value=(id,)
        self.cursor.execute(sql,value)  
        try:
            obj=self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Err: ",err)

    def getStudentByClassId(self,classid):  
        sql="Select * from student where classid =%s"
        value=(classid,)
        self.cursor.execute(sql,value)  
        try:
            obj=self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Err: ",err)
    
    def getClasses(self):
        sql="Select * from class"
        self.cursor.execute(sql)  
        try:
            obj=self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Err: ",err)

    def deleteStudent(self,studentid):
        sql="delete from student where id = %s"
        #self.name değil student.name yapmamızın amacı dışarıdan gönderdiğimiz obje üzerinde işlem yaptığımız için
        value=(studentid,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi")
        except mysql.connector.Error as err:
            print('hata: ',err)

    def addStudent(self,student:Student):  
        sql="INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender,classId) Values (%s,%s,%s,%s,%s,%s)"
        #self.name değil student.name yapmamızın amacı dışarıdan gönderdiğimiz obje üzerinde işlem yaptığımız için
        value=(student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print('hata: ',err)
    
    def editStudent(self,student:Student):
        sql="UPDATE student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s,classid=%s where id=%s"
        #self.name değil student.name yapmamızın amacı dışarıdan gönderdiğimiz obje üzerinde işlem yaptığımız için
        value=(student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print('hata: ',err)
        

    def addTeacher(self,teacher:Teacher):
        pass
    def editTeacher(self, teacher: Teacher):
        pass

    # def __del__(self):
    #   self.connection.close()
        print('db silindi')
    

db = DbManager()

# 6. kayıttan bilgileri alıyoruz
# student = db.getStudentById(6)
# # 6. kayıttaki bilgileri kullanarak yeni bir student insert işlemi yapıyoruz bu yüzden tüm bilgileri göndermemiz gerekmiyor
# student[0].name="Çınar"
# student[0].surname="Turan"
# student[0].studentNumber="501"
# db.addStudent(student[0])

# UPDATE İŞLEMİ
# student = db.getStudentById(13)
# student[0].name="Enes"
# db.editStudent(student[0])


# students=db.getStudentByClassId(1)
# print(students[0].name)
# print(students[4].name)

