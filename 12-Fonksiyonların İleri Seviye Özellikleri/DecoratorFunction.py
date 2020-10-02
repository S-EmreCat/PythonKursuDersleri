## bir fonksiyona özellik eklemek istediğimiz zaman kullanırız

# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator   ####  bu şekilde yaparsak  say_hello=my_decorator(say_hello)  atamasını otomatik yaparız

# def say_hello(name):    ##  bize dışarıda say helloyu çağırmak kalır
#     print("Hello",name)     ##        say_hello ya parametre göndermek istersek   decoratorda  wrapper a da name parametresini göndermeliyiz
# say_hello("ali")          #### tüm çıktıyı alırız
# def sayGreeting():
#     print("greeting")

# sayGreeting=my_decorator(sayGreeting)
# sayGreeting()
# say_hello=my_decorator(say_hello)         ### bu şekilde yaptığımızda 2 farklı hello ve greeting fonksiyonlarına
# say_hello()                             ### decorator ile ekstra özellikler kazandırdık

import math
import time
def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)  
        func(*args,**kwargs)
        finish=time.time()
        print("fonksiyon "+func.__name__+ str(finish-start)+" saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
    
usalma(2,3)
faktoriyel(4)








