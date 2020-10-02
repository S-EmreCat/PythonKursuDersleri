# def sayHello(name = '  user  '):   # parametre default olarak böyle tanımlanır
#     print("Hello "+ name)
# sayHello('emre')
# sayHello()

def geridonmeliFonk(name='user'):
    '''
    sdahfkglkjfd
    '''
    return 'Hello ' + name

# print ile ekrana yazdırmayıp geri döndürdüğümüz için bir değişkene atıyoruz
msg=geridonmeliFonk(' Emre')
print(msg)
print(help(geridonmeliFonk))