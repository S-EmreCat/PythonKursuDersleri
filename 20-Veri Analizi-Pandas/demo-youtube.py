import pandas as pd
import numpy as np
df=pd.read_csv("youtube-ing.csv")


# 1- İlk 10 kaydı getiriniz.
result=df.head(10)
# 2- İkinci 5 kaydı getiriniz.
result=df[5:15].head(5)
# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
# result=len(df.columns) >> 16
# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
# result=df.drop(columns=['thumbnail_link','comments_disabled',"ratings_disabled","video_error_or_removed","description"],axis=1)

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
# like=df['likes'].mean()
# dislile=df['dislikes'].mean()
# print(like) 134519.55349984582
# print(dislile) 7612.559975331483

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
# result=df[['likes','dislikes']].head(50) 

# 7- En çok görüntülenen video hangisidir ?
result=df[df['views']==df['views'].max()]['title'].iloc[0]     #Nicky Jam x J. Balvin - X (EQUIS) | Video Ofic...

# 8- En düşük görüntülenen video hangisidir?
# result=df[df['views']==df['views'].min()]['title'].iloc[0]      #Mountain Bikers Worried About Military Land Being Fenced Off
# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result=df.sort_values(by=['views'],ascending=False).head(10)
# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result=df.groupby('category_id').mean().sort_values('likes')['likes']
# 11- Kategoriye göre yorum sayılarını sıralayınız.
result=df.groupby('category_id')['comment_count'].sum()
# 12- Her kategoride kaç video vardır ?
result=df.groupby('category_id')['video_id'].count()
result=df['category_id'].value_counts()
# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df['Title_len']=df["title"].apply(len)
result=df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
df['tag_count']=df['tags'].apply(lambda x:len(x.split('|')))
result=df

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

print(result)