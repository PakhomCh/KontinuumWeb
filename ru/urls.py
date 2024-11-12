from django.urls import path
from django.shortcuts import redirect

from . import views

app_name = 'ru'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:any>/home', lambda reqest, any: redirect('/')),
    path('<str:any>/lore', lambda reqest, any: redirect('/lore')),
    path('<str:any>/news', lambda reqest, any: redirect('/news')),
    path('<str:any>/login', lambda reqest, any: redirect('/login')),
    path('<str:any>/legal', lambda reqest, any: redirect('/legal')),
    path('dynastika/', views.dynastika, name='dynastika'),
    path('ascention/', views.ascention, name='ascention'),
]