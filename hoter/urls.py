"""
URL configuration for hoter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hazbin import views
from django.conf.urls.static import static

from . import settings 

urlpatterns = [
    path('', views.homepage, name='homepage'),  
    path('admin/', admin.site.urls),
    path('create/', views.createpage, name= "createpage"),
    path("log/", views.logpage, name="logpage"),
    path("registration/", views.registerpage, name= "register"),
    path("hotelrooms/", views.hotelroomspage, name= "hotelrooms"),
    path("delete/", views.deletepage, name="delete"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

''' path('registrations/', views.RegistrationListView.as_view(), name='registration_list'),
    path('registrations/create/', views.RegistrationCreateView.as_view(), name='registration_create'),
    path('registrations/<pk>/update/', views.RegistrationUpdateView.as_view(), name='registration_update'),
    path('registrations/<pk>/delete/', views.RegistrationDeleteView.as_view(), name='registration_delete'),'''