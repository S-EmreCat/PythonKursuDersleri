from django.urls import path
from . import views

# root http://127.0.0.1:8000//movies
#      http://127.0.0.1:8000/movies/2
#      http://127.0.0.1:8000//movies/search
urlpatterns =[
    path('', views.index , name='movies'),
    path('search' ,views.search, name='search'),
    path('<int:movie_id>', views.detail , name='detail')
]