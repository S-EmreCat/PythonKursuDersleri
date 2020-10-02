import pymongo
# id ile filtreleme yapılırken ObjectId func kullanırız
from bson.objectid import ObjectId

# mongodb diğer işlemler için siteden yardım al

myclient=pymongo.MongoClient("mongodb+srv://emrecat:jnikrorqHBu9gr0i@cluster0.gfzh9.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=myclient["node-app"]
mycollection=mydb["products"]

filter={"name":"Samsung S5"}
# tek kayıt döneceğinden eminsek find_one func ile işlem yapabiliriz
# result=mycollection.find_one(filter)
# print(result)
# kayıt sayısından emin değilsek
# result=mycollection.find(filter)
# for i in result:
#     print(i)

# id ye göre filter
# result=mycollection.find_one({"_id":ObjectId("5f575c8174d245c6a5edf481")})
# print(result)

# in metodu ile sorgu yapma
# result=mycollection.find({
#     "name":{
#         "$in":["Samsung S5","Samsung S6"]
#     }
# })

# price >2000 sorgusu grater than (gt)  ||||||  price >= 2000 gte grater than equal --büyük eşit
# result=mycollection.find({
#     "price":{
#         "$gt":2000
#     }
# })

# equal eşittir 
result=mycollection.find({
    "price":{
        "$eq":2000
    }
})

for i in result:
    print(i)

