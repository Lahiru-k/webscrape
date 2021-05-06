from django.urls import path
from . import views

app_name = "webscraper"

urlpatterns = [
    path('', views.home, name='index'),
]
