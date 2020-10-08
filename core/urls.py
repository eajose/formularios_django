from django.urls import path

from . import views

urlpatterns = [
    path('pessoa/', views.pessoa, name='pessoa'),
    path('endereco/', views.endereco, name='endereco'),
]
