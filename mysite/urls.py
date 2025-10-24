from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Halo Dunia! Ini halaman utama Django 😊")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # 👈 ini route untuk halaman utama /
]
