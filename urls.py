
from django.urls import path
from . import views     
    
urlpatterns = [
    path('', views.index),
    path('adddojo', views.adddojo),
    path('addninja', views.addninja),
    path('delete_user', views.delete_user),
    
    
]
