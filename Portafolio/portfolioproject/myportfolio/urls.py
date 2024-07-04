from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='index'),
    #path('contacto/', views.contacto, name='contacto'),
]