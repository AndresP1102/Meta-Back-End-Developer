from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name="home"),
        path('aboutus/', views.aboutus, name="aboutus"),
        path('menu/', views.menu, name="menu"),
        path('book/', views.book, name="book"),
        path('drinks/<str:drink_name>/', views.drinks, name="drink"),
]