import pymongo
from bson.objectid import ObjectId

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
myclient=pymongo.MongoClient("mongodb+srv://emrecat:jnikrorqHBu9gr0i@cluster0.gfzh9.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print('*'*50)

# result=mycollection.delete_one({"name":"IPhone 8"})
# result =mycollection.delete_many({"name": {"$regex":"^S"}})  # s ile başlayan kayıtları siler
result = mycollection.delete_many({})

print(f'{result.deleted_count} adet kayıt silindi.')

for i in mycollection.find():
    print(i)