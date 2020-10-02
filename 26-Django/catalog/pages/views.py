from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# hangi html sayfasını getirmek istiyorsak onun için işlem yapıyoruz

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')