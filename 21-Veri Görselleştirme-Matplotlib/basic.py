#pip install matplotlib yazarak kurulup yapıyoruz
import matplotlib.pyplot as plt
import numpy as np
###      https://matplotlib.org/  sitesinden detaylı grafik örneklerine ulaşılabilir    ####
# grafik oluşturma
""" x=[1,2,3,4]
y=[1,4,9,16]
# plt.plot(x,y,color="red",linewidth="5")  # grafik çizgisi için renk ve kalınlık ataması yapılabilir
plt.plot(x,y,"o--g") # şeklinde özel still atamaları yapılabilir sitede mevcut
plt.axis([0,6,0,20])  # grafik sınırlarını belirleyebiliriz x=0-6  y=0-20 arasında değişir
plt.title("Grafik Başlığı")
plt.xlabel("x label deneme")
plt.ylabel("y label deneme")
plt.show() """

###  3 tane farklı grafiği aynı bölgede gösterme işlemi
""" x=np.linspace(0,2,100)
plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")
plt.xlabel("x label")
plt.ylabel("y label")
plt.legend() # sol üst köşede isimlendirmeler bulunur
plt.show() """

### 
# plt.subplot(2) #  birden fazla grafiği alt alta oluşturmak istersek
""" x=np.linspace(0,2,100)
fig,axs = plt.subplots(3) 
axs[0].plot(x,x,color="red")
axs[0].set_title("axs 0 title")
axs[1].plot(x,x**2,color="green")
axs[1].set_title("axs 1 title")
plt.tight_layout() # başlıklar birbirine girmesin boşluk bırakılsın diye yazdık
plt.show() """

# 
""" x=np.linspace(0,2,100)
fig,axs = plt.subplots(2,2) 
fig.suptitle("grafik başlığı")
axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="green")
axs[1,1].plot(x,x**3,color="orange")
axs[1,0].plot(x,x**4,color="yellow") """

import pandas as pd
df=pd.read_csv("nba.csv")
df=df.drop('Number',axis=1).groupby('Team').mean()
df.head(5).plot(subplots=True) # her kolonun grafik başlığını ayrı atar True yaptığımız için
plt.legend()


plt.show()
