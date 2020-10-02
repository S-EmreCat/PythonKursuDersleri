# def add(a, b):
#     return sum((a,b))

# print(add(32,2))

# def toplama(*parametreler):   # istediğimiz kadar parametre gönderebiliriz bu şekilde  touble list oluşturur
#     return sum(parametreler)

# print(toplama(20,32,2,65,85))

# def displayUser(**parametreler):     #########     ** şeklinde parametre gönderirsek dictionary şeklinde çıktı alırız
#     print(type(parametreler))
#     for key, value in parametreler.items():
#         print("{} is {}".format(key,value))

# displayUser(name='çınar', age=2, city='Istanbul')
# displayUser(name='çınaasdhfgr', age=2, city='Istaasgdfgnbul', tel='235456')
# displayUser(name='emre', age=2, city='bursa' , adress="sdfhghj")

# def myfunc(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# myfunc(10,20,2,3,30,40,50,key1='value 1',key2='vvalue2 2')
