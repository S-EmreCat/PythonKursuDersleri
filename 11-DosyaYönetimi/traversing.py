file=open("newfile.txt","r",encoding='utf-8')
content=file.read()
print(content)
file.close()

########       with    ile kapatmanın kısa yolu::

with open("newfile.txt","r",encoding='utf-8') as file:    ### within yanına açtığımız dosyası kapatır kendi otomatik
    content= file.read(10)
    print(content)
    print(file.tell()) ###3 tell fonksiyonu   cursor un nerede olduğu bilgisini verir
    file.seek(5)        #####    cursoru istediğimiz noktaya gönderiririz
    print(file.tell())
    content2=file.read(10)
    print(content2)