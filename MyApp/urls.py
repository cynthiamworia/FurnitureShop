from django.urls import path
from MyApp import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('furniture/', views.furniture, name='furniture'),
    path('shop/', views.shop, name='shop')

]
