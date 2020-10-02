import pandas as pd
import numpy as np

data=pd.read_csv('player_data.csv')
data.dropna(inplace=True) # 
data['name']=data['name'].str.upper() # tüm isimleri bütük harf yapar
print(data.head(10))