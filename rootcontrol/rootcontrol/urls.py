from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),

    #path Datacenter
    path('datacenters/', views.datacenters, name='datacenters'),
    
    path('logbook/', views.logbook, name='logbook'),
    
]
