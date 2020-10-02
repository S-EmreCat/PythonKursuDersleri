# # x=10
# # if x > 5::
# #     raise Exception("x 5den büyük değer alamaz")

# def checkPassword(psw):
#     import re
#     if len(psw)<8:
#         raise Exception("parola en az 7 karakterden oluşmalıdır.")
#     elif not re.search("[a-z]",psw):
#         raise Exception("parola küçük harf içermelidir.")
#     elif not re.search("[0-9]",psw):
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("parola alpha numeric karakter içermelidir.")
#     elif re.search("\s",psw):     #\s boşluk karakteri
#         raise Exception("parola boşluk  içermemelidir.")
    
# parola="12345B6_a78"
# try:
#     checkPassword(parola)
# except Exception as ex:
#     print(ex)
# else:
#     print(f"parolanız oluşturuldu: {parola} ")
    

class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("name alanıfazla karakter")
        else:
            self.name=name
p=Person("Aliiiiiiiiii",1995)
