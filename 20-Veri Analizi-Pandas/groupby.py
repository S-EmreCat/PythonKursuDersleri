import pandas as pd
import numpy as np

personeller={
    'Çalışan': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman':['İnsan Kaynakları','Bilgi İşlem', 'Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş':[30,25,45,50,23,34,42],
    'Semt':['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe.','Tuzla','Kadıköy'],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
}

df=pd.DataFrame(personeller)

# result=df
# result=df['Maaş'].sum() # tüm maaşların toplamı
# result=df.groupby("Departman").groups # departmana göre gruplama
# result=df.groupby(["Departman","Semt"]).groups 
# Semtleri aynı olan çalışanlara for döngüsü ile ulaşıyoruz
# semtler=df.groupby('Semt')
# for name,group in semtler:
#     print(name)
#     print(group)
# Departmanları aynı olan çalışanlara for döngüsü ile ulaşıyoruz
# departmanlar=df.groupby('Departman')
# for name,group in departmanlar:
#     print(name)
#     print(group)
# result=df.groupby('Semt').get_group("Kadıköy") # semti Kadıköy olan kişiler
# result=df.groupby('Departman').get_group("Muhasebe")

# result=df.groupby('Departman').sum() # kolon belirtmediğimiz için yaş ve maaşları ayrı ayrı toplayıp ekrana yazdırdı

# result=df.groupby('Departman').mean() # ortalama

# result=df.groupby('Departman')['Maaş'].sum() # maaşların toplamı
# result=df.groupby('Semt')["Yaş"].mean()  # semtlere göre yaş ortalamaları
# result=df.groupby('Semt')['Çalışan'].count() # semtlere göre kişi sayısı
# result=df.groupby('Departman')["Maaş"].max()  # tüm departmanların en büyük maaşa sahip kişileri
# result=df.groupby('Departman')["Maaş"].max()['Muhasebe']  #Muhasebe departmanının max maaşlı kişisi
# result=df.groupby('Departman').agg(np.mean)  # nump ile birlikte daha kolay kullanım !! kolon belirtmediğimiz için yaş ve maaşları ayrı ayrı toplayıp ekrana yazdırdı

# result=df.groupby('Departman')['Maaş'].agg([np.sum,np.max,np.min,np.mean]) # numpy ile birden fazla sonucu tek tabloda yazdırma
result=df.groupby('Departman')[['Maaş']].agg([np.sum,np.max,np.min,np.mean]).loc['Muhasebe'] # sadece muhasebe için yazdırma
print(result)