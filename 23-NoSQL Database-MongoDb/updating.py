import pymongo
# id ile filtreleme yapılırken ObjectId func kullanırız
from bson.objectid import ObjectId


myclient=pymongo.MongoClient("mongodb+srv://emrecat:jnikrorqHBu9gr0i@cluster0.gfzh9.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=myclient["node-app"]
mycollection=mydb["products"]

# update_one
# mycollection.update_one(
#     {"name":"Samsung S5"},
#     {"$set":{
#         "name":"Iphone 6"
#     }}
# )

mycollection.update_one(  # update_one ile işlem yaptığımız için bulduğu ilk kayıt üzerinde işlem yapıyor diğer aynı bilgiye sahipler değişmiyor
    {"name":"Samsung S6"},  ## ilk {} de nereyi güncelleyeceğimizi belirtiyoruz
    
    # 2. {} de hangi işlemleri yapacağımızı belirtiyoruz
    {"$set":{
        "name":"Iphone 7",
        "price": 4500
    }}
)



# for i in mycollection.find():
#     print(i)



#update_many
 # tüm s7 ler değişir

query={"name":"Iphone 4"}
newvalues={"$set":{
    "name":"Samsung S11",
    "price":3000
}}
# dışarıda belirleyip fonksiyona değişken olarak gönderebiliriz
result=mycollection.update_many(query,newvalues)
print(f"{result.modified_count} adet kayıt güncellendi")

# mycollection.update_many(
#     {"name":"Samsung S7"},
#     {"$set":{
#         "name":"Iphone 8",
#         "price":7000
#     }}
# )

for i in mycollection.find():
    print(i)