import pymongo
# id ile filtreleme yapılırken ObjectId func kullanırız
from bson.objectid import ObjectId

# mongodb diğer işlemler için siteden yardım al

myclient=pymongo.MongoClient("mongodb+srv://emrecat:jnikrorqHBu9gr0i@cluster0.gfzh9.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=myclient["node-app"]
mycollection=mydb["products"]


# sıralama işlemi name için
# result=mycollection.find().sort('name',-1) # büyükten küçüğe sıralamak için -1 
# for i in result:
#     print(i)

# result=mycollection.find().sort('price',1) # küçükten büyüğe sıralamak için 1  ++++ default hali 1 
# for i in result:
#     print(i)

# isimler büyükten küçüğe ---- fiyatlar azalan
result=mycollection.find().sort([('name',-1),("price",1)]) # büyükten küçüğe sıralamak için -1 
for i in result:
    print(i)