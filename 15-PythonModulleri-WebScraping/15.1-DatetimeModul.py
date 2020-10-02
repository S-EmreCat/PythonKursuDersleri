from datetime import datetime
from datetime import timedelta #  modülün içinden tek bir classı import etmek istersek

# import datetime

# datetime modülünün içindeki datetime classının now fonksiyonu  >> 2020-08-17 10:36:10.886719
# simdi=datetime.datetime.now()  # today de now ile aynı sonucu verir

# #  tarihin kaçıncı gün olduğu bilgisi
# result=datetime.datetime.today().day #year,minuteihour,second, month

# # c time daha açıklayıcı bir çıktı verir
# result=datetime.datetime.ctime(simdi)  # >>  Mon Aug 17 10:40:08 2020  

# result=datetime.datetime.strftime(simdi,'%x')  # tarihi istediğimiz formatta string olarak yazdırırız
# dt=datetime.strptime(t,'%d %b %Y hour %H:%M:%s')

# print(dt)
simdi=datetime.now()
birtday=datetime(1997,1,25)
result=datetime.timestamp(birtday) # ilgili tarih saniye cinsinden getirilir.  # 1970 ile arasındaki fark
result=datetime.fromtimestamp(result) # saniyeye tarihe çevirir
result=simdi-birtday  # 2 tarih arasındaki gün farkı  timedelta
result=result.seconds  # farkı saniyeye dönüştürür
result=simdi+timedelta(days=10)  # şuan ki tarihe 10 gün ekledik
result=simdi+timedelta(days=730,minutes=10)
result=simdi-timedelta(days=10)   # şuan ki tarihten 10 gün çıkarttık

print(result)