## catolog dosyasını ilk oluşturduğumuzda buna benzer bir urls.py ekleniyor otomatik olarak
## burada ise kendimiz ekleme yapıyoruz

# path göstermek için import path yapıyoruz
from django.urls import path
# pages klasörü içerisindeki views.py den index fonksiyonuna ulaşıyoruz 
# aynı dizinde olduğumuz için . ile ulaşıyoruz
from . import views

# http://127.0.0.1:8000/

urlpatterns=[
    path('', views.index, name='index'),
    path('about',views.about,name='about')
     ## direkt olarak http://127.0.0.1:8000/ adresine ulaşmak istediğimiz için ilk kısmı boş geçiyoruz  eğer http://127.0.0.1:8000/index adresine ulaşmak isteseydik path('index',views.index,name='index') şeklinde çağırırdık
    # about sayfasına ulaşmak için ise http://127.0.0.1:8000/about şeklinde ulaşılır
]