from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('home/')),
    path('home/', views.index),
]
