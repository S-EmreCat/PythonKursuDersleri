# try:
#     file=open("newfile.txt","r",encoding='utf-8')   ### r modunu yazmasak bile default mod r   dir.
#     print(file)
# except Exception as exx:
#     print("bu dosya mevcut konumda yoktur.",exx)
# finally:
#     print("dosya kapatılıyor.")
#     file.close()

# file=open("newfile.txt","r",encoding='utf-8')

# print(file.readline(),end="")
# print(file.readline(),end="")          ##  satır satır okumayı sağlar
# print(file.readline(),end="")            ####   readline()
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")  
# print(file.readline())  
# print(file.readline())      # end=" "   yazmazsak dosya bittikten sonra boşluk koyup devam eder
# print(file.readline())  
# print(file.readline())  

# # for döngüsü ile okuma 
# for i in file:
#     print(i,end=" ")
# file.close()

# read fonksiyonu ile okuma

# content1=file.read()
# print(" içerik 1 ")
# print(content1)


# file=open("newfile.txt","r",encoding='utf-8')  # 2. kez başa döndürüp tekrar okutmak için tekrar open yaparız
# content2=file.read()
# print(" içerik 2 ")
# print(content2)

# content=file.read(5)
# content=file.read(3)  ###  cursor kaldığı yerden devam ettiği için 5-8 . karakterleri okur
# print(content)
# file.close()


file=open("newfile.txt","r",encoding='utf-8')

liste=file.readlines()      ### her satırı ayrı bir eleman olarak alıp listeye atar

print(liste)
print(liste[4])   # istersek index index satırlara ulaşırız bu sayede