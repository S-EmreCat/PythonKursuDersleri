import pymongo
from bson.objectid import ObjectId


myclient=pymongo.MongoClient("mongodb+srv://emrecat:jnikrorqHBu9gr0i@cluster0.gfzh9.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=myclient["node-app"]
mycollection=mydb["products"]

# tekli kayıtla ilgilenirken bulduğu ilk kaydı getirir
result=mycollection.find_one()
# çoklu kayıt select * gibi düşün
# for i in mycollection.find(): # find içerisine koşul göndermediğimiz için tüm kayıtları getirir
#     print(i)
#  0 ataması yapılırsa o bilgi getirilmez 1 ataması yapılanlar getirilir
#  ilk {} koşul belirtmek için 2. {} sütun için
#
 
for i in mycollection.find({},{"_id":0,"name":1,"price":1}): 
    print(i)