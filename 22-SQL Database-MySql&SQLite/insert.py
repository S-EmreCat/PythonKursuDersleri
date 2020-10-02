import mysql.connector 

# tek bir ürün ekleyen fonksiyon
def insertProduct(name,price,imageUrl,description):
    connection=mysql.connector.connect(host="localhost",user="root", password="mysql1234",database="node-app")
    cursor=connection.cursor()

    sql="INSERT INTO products(name,price,imageUrl,description) Values (%s,%s,%s,%s)"
    values=(name,price,imageUrl,description)
    cursor.execute(sql,values)
     # commit yaparak database'e sorgumuzu gönderiyoruz
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id numarası: {cursor.lastrowid} ")
    except mysql.connector.Error as err:
        print('hata: ',err)
    finally:
        connection.close() # bağlantıyı kapatmamız lazım
        print("database bağlantısı kapandı.")
# birden fazla ürünü ekleyen fonksiyon
def insertProducts(list):
    connection=mysql.connector.connect(host="localhost",user="root", password="mysql1234",database="node-app")
    cursor=connection.cursor()

    sql="INSERT INTO products(name,price,imageUrl,description) Values (%s,%s,%s,%s)"
    values=list
    cursor.executemany(sql,values)  ## birden fazla işlem yaptığımızı belirtmek için executemany fonksiyonu kullanılıyor
    connection.commit() # commit yaparak database'e sorgumuzu gönderiyoruz
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id numarası: {cursor.lastrowid} ")
    except mysql.connector.Error as err:
        print('hata: ',err)
    finally:
        connection.close() # bağlantıyı kapatmamız lazım
        print("database bağlantısı kapandı.")

def getProducts():
    connection=mysql.connector.connect(host="localhost",user="root", password="mysql1234",database="node-app")
    cursor=connection.cursor()
    # cursor.execute("SELECT * from products where name='samsung s8'")
    
    # %Samsung => başta başka karakterler olsun sonu Samsung ile bitsin
    # Samsung% => Samsung ile başlasın devamı önemsiz
    # %Samsung% herhangi bir yerinde Samsung olsun
    cursor.execute("SELECT * from products") # ismin içinde kelime ararken LIKE kullanılır
    # cursor.execute("SELECT * from products Order By name,price") ## order by ile sıralama yapabiliriz
    # cursor.execute("SELECT name,price from products where id=1")  # database çok işlem yapmaması için işlem yapılacak kolonlar seçilebilir
    result=cursor.fetchall() # tüm kayıtları getirir
    # result=cursor.fetchone() # bulduğu ilk kaydı getirir
    # print(f"name: {result[0]} fiyatı: {result[1]} ")
    # print(result)
    # print(result[0]) # istediğimiz indisli elemana ulaşabliriz
    for i in result: 
        # print(i) # tüm ürünler
        print(f" id: {i[0]} name: {i[1]} fiyatı: {i[2]} ") # ürünlerin istediğimiz özelliğine ulaşma şekli  
# getProducts()



# list=[]
# while True:

#     name=input("ürün adını giriniz")
#     price=input("ürün fiyatını giriniz")
#     imageUrl=input("ürün fotosu giriniz")
#     description=input("ürün tanımı giriniz")
#     list.append((name,price,imageUrl,description)) #tuple olarak ekliyoruz
#     result=input("devam etmek istiyor musunuz(e/h)")
#     if result=="h":
#         print("kayıtlarınız veri tabanına aktarılıyor")
#         print(list)
#         #kayıt
#         insertProducts(list=list)
#         break

# insertProduct(name,price,imageUrl,description)

########################################################################
########################################################################

########################################################################

########################################################################



def getProductById(id):
    connection=mysql.connector.connect(host="localhost",user="root", password="mysql1234",database="node-app")
    cursor=connection.cursor()
    
    sql ="SELECT * from products where id=%s"
    params=(id,) 
    cursor.execute(sql,params)
    result=cursor.fetchone()
    print(f" id: {result[0]} name: {result[1]} price: {result[2]} ")

# getProductById(1)


## UPDATE SORGUSU- KAYIT GÜNCELLEME
def updateProduct(id,name,price):
    connection=mysql.connector.connect(host="localhost", user="root",password="mysql1234",database="node-app")
    cursor=connection.cursor()
    sql="update products Set name=%s,price=%s where id=%s"
    values=(id,name,price)
    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"id : {id} olan kayıt güncellendi")
    except mysql.connector.Error as err:
        print(err)
    finally:
        connection.close()
        print("baglantı kapatıldı")

# updateProduct(1,"Iphone 8",6000)

def deleteproduct(id):
    connection=mysql.connector.connect(host="localhost", user="root",password="mysql1234",database="node-app")
    cursor=connection.cursor()
    sql="delete from products where id='%s'"
    value=(id,)
    # sql="delete from products where name LIKE '%s7%' " # aramaya göre de delete yapabiliriz
    cursor.execute(sql,value)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as err:
        print(err)
    finally:
        connection.close()
        print("baglantı kapatıldı")
# deleteproduct(7)
# getProducts()


## 22.22 ilişkili tablolardan veri seçme
def getProducts22Video():

    connection=mysql.connector.connect(host="localhost",user="root", password="mysql1234",database="node-app")
    cursor=connection.cursor()
    # join işlemi
    # sql="SELECT * from products inner join categories on categories.id=products.categoryid"
    # sql="SELECT products.name,products.price,categories.name from products inner join categories on categories.id=products.categoryid"
    sql="SELECT * from products inner join categories on categories.id=products.categoryid where categories.name='telefon'"
    cursor.execute(sql)
    
    try:
        result=cursor.fetchall() 
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print(err)
    finally:
        connection.close()
        print("baglantı kapatıldı")
getProducts22Video()