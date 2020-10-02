mylist=[1,2,3]
# print(len(mylist))
# myString='my String'
# print(len(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie öznesi oluşturuldu")

m=Movie("film adı","yönetmen","süre")
print(str(mylist))
print(str(m))

del m   # objeyi siler

print(m)
