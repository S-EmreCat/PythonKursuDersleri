import pandas as pd

customersA={
    'CustomerId':[1,2,3,4],
    'FirstName':['Ahmet','Ali','Hasan','Canan'],
    'LastName':['Yılmaz','Korkmaz','Çelik','Toprak']
}
customersB={
    'CustomerId':[5,6,7,8],
    'FirstName':['Yağmur','Çınar','Cengiz','Can'],
    'LastName':['Bilge','Turan','Yılmaz','Turan']
}

orders={
    "OrderId":[10,11,12,13],
    "CustomerId":[1,2,5,7],
    "OrderDate":['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}


df_customersA=pd.DataFrame(customersA,columns=['CustomerId','FirstName','LastName'] )
df_customersB=pd.DataFrame(customersB,columns=['CustomerId','FirstName','LastName'] )
df_orders=pd.DataFrame(orders,columns=["OrderId", "CustomerId","OrderDate"] )

result=pd.merge(df_customersA,df_orders,how='inner')
result=pd.merge(df_customersA,df_orders,how='left')
result=pd.merge(df_customersA,df_orders,how='right')

result=pd.concat([df_customersA,df_customersB])  # 2 dataframe i concat fonk ile topluyoruz

print(df_customersA)
print(df_customersB)
print(df_orders)
print(result)
