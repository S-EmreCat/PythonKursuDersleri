import pandas as pd

df=pd.read_csv('imdb.csv')

# 1- Dosya hakkındaki bilgiler
result=df
result=df.info
result=df.columns
# 2- ilk 5 kayıt
result=df.head(5)
# 3- ilk 10 kayıt
result=df.head(10)
# 4- son 5 kayıt
result=df.tail(5)
# 5- son 10 kayıt
result=df.tail(10)
# 6- Sadece Movie_Title column 
result=df["Movie_Title"]
# 7- Sadece Movie_Title  column ilk 5 kayıt
result=df["Movie_Title"].head(5)
# 8- Sadece Movie_Title ve Rating column  ilk 5 kayıt
result=df[["Movie_Title","Rating"]].head(5)
# 9- Sadece Movie_Title ve Rating column son 7 kayıt
result=df[["Movie_Title","Rating"]].head(5)
# 10- Sadece Movie_Title ve Rating column ikinci 5 kayıt
result=df[5:][["Movie_Title","Rating"]].head(5)
# 11- Sadece Movie_Title ve Rating column içeren ve imdb >= 8.0 olan ilk 50 kayıt
result=df[df["Rating"]>=8.0][["Movie_Title","Rating"]].head(50)
# 12- Yayın tarihi 2014 il 2015 arasında olan filmler
result=df[ (df["YR_Released"]>=2014) & (df["YR_Released"]<=2015)][["YR_Released","Movie_Title"]]
# 13- Num_Reviews 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmler
# query ile de aynı şeyleri yapabiliriz
result=df[(df["Num_Reviews"]>100000) | (df["Rating"]>=8) & (df["Rating"]<=9)]
result=df.query("Num_Reviews>100000 | Rating >=8  & Rating <=9")
print(result)