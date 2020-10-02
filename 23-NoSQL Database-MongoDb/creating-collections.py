

import pymongo

myclient=pymongo.MongoClient("mongodb+srv://emrecat:jnikrorqHBu9gr0i@cluster0.gfzh9.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=myclient["node-app"]  # database yoksa oluşturup bağlanır varsa direkt bağlanır

mycollection=mydb["products"] # collection yoksa oluşturur

# print(mydb.list_collection_names()) # collections list

# product= {"name":"Samsung S5","price":2000}
# istersek kendimiz id tanımlaması yapıp sitenin yaptığı tanımlamayı ezebiliriz.
# product= {"_id":1,"name":"Samsung S5","price":2000}
# result=mycollection.insert_one(product) # 1 kayıt ekleyeceğimiz için insert_one func kullanıyoruz 
# # mycollection.insert_many(product)  # birden fazla kayıt ekleyeceksek many func kullanılır
# print(result) # bir nesne geri dönderir
# print(type(result))
# # mongo her ürüne kendisi bir id ataması yapar ulaşmak için:
# print(result.inserted_id)


productList=[
    {"name":"Samsung S6", "price":3000,"description":"iyi telefon"},
    {"name":"Samsung S7", "price":4000,"categories":["telefon","elektronik"]}
]
results=mycollection.insert_many(productList)
print(results.inserted_ids)