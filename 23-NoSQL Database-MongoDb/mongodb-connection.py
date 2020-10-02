# pip install pymongo  ile console üzerinden yükleme yapılır
# Mongo Atlas üzerindeki database'e ulaşabilmek için pip instal pymongo[srv] kurulumu yapılır

import pymongo


        # # MongoDB Compass üzerindeki database bağlantısı



# myclient=pymongo.MongoClient("mongodb://localhost:27017")
# mydb=myclient["node-app"] 
# print(myclient.list_database_names()) # database listesine ulaşırız




    # site üzerindeki database bağlantısı


# 1- Clusters kısmında connect yaptıktan sonra app ile bağlanmayı seçip linki kopyalayıp fonksiyon içine yapıştırıyoruz
# 2- dbname kısmına kendi database ismimizi yazıyoruz
# 3- password kısmına siteden aldığımız şifreyi yapıştırıyoruz
myclient=pymongo.MongoClient("mongodb+srv://emrecat:jnikrorqHBu9gr0i@cluster0.gfzh9.mongodb.net/node-app?retryWrites=true&w=majority")
mydb=myclient["node-app"] 
print(myclient.list_database_names())