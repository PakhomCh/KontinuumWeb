from django.urls import path

from . import views

app_name = "ascention"
urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
]