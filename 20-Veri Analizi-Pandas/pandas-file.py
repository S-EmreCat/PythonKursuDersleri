import pandas as pd 
# dosyayı klasöre ekliyoruz ve read_csv ile okuyoruz

# csv dosyalarının okunması
# df=pd.read_csv('player_data.csv')

# json dosyalarının okunması
# df=pd.read_json('sample.json',encoding='utf-8')

# excel den okuma 
# df=pd.read_excel('sample.xlsx')

# sql den okuma yapma öncelikle pip install pysqlite3 yapıp kütüphaneyi kuruyoruz
# connection=sqlite3.connect('sample.db')
# df=pd.read_sql_query('SELECT * FROM students')


# print(df)