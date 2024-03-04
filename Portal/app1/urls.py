from django.urls import path
from . import views

urlpatterns = [
    path('HelloWorld/', views.HelloWorld, name="HelloWorld"),
    path('main/', views.main_view, name="main"),
]
