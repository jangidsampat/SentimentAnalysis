from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('output/', views.printResult, name='output'),
]