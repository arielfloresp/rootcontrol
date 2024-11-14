from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dash/', views.dash, name='dash'),
    
    path('logbook/', views.logbook, name='logbook'),
    
]