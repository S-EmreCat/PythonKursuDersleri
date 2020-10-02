import re 

# re modülü

# str ="Python Kursu: Python Programlama Rehberiniz | 40 saat"
# result=re.findall("Python",str)  # verilen str içindeki pythonları bulup bir diziye atar
# result=len(result) # buradan kaç tane olduğunu bulabilirizz

# re.split()
# result=re.split(" ",str) # her boşluk karakterinde ayırır
# result=re.sub(" ","-",str)  # boşluk karakterlerini - karakteri ile değişir   \s boşluk demek

# re.search()
# result=re.search("Python",str) # >> <re.Match object; span=(0, 6), match='Python'>    span: 0-6. indislerde ilk Python bulunmuş
# result=result.span() #>> (0, 6)
# result=result.start()  # >> spanın ilk indisini verir
# result=result.end() # >> spanın son indisini verir
# result=result.string  ##   hangi string ifadenin içerisinde aradığımızı verir
# result=result.group()  ## > hangi kelimeyi aradığımızı verir
# print(result)


str ="Python Kursu: Python Programlama Rehberiniz | 40 saat"

# result=re.findall("[a-e]",str) # str içindeki a dan e ye kadar tüm karakterleri arar bir liste ile sonuç verir
# result=re.findall("[0-5]",str)  # 0 dan 5 e kadar
##    0-39 dersek => 01239 karakterlerini arar
##    [^abc] => abc dışındaki karakterler
##    [^0-9] => rakam olmayan karakterler

# result=re.findall("...",str)   # string i 3er karakterli gruplara ayırıp listeye atar
# result=re.findall("Py..on",str)  ## string içerisinde Py ile başlayıp on ile biten arada random 2 karakterin olduğu şeyleri arar

# result=re.findall("^Python",str) ## gönderdiğimiz string sorduğumuz karakter ile başlıyor mu
# result=re.findall("saat$",str) ## gönderdiğimiz string sorduğumuz karakter ile bitiyor mu
# print(result)




