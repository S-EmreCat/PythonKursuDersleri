website="https://www.sadikturan.com"
course= "Pyton Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#2
# website=website.replace(https://," "),(.com," ")
# print(website)

#3
course=course.lower()
print(course)
#4

sayi=website.count("a")
print(f"{sayi}tane a vardır.")
#5

isBas=website.startswith("www")
isBit=website.endswith(".com")
print(isBas,isBit)

#6
varMi=website.find(".com")
print(varMi)
#7
alfa=course.isalpha()
print(alfa)

#8
yazi="Contents"
yazi=yazi.center(50,"*")
print(yazi)
#9
course=course.replace(" ","-")
print(course)
#10
hello="Hello World"
hello=hello.replace("World","There")
print(hello)