from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', admin.site.urls),
    path('pessoa/', views.PessoaCreateView.as_view(), name='pessoa'),
    path('endereco/', views.EnderecoCreateView.as_view(), name='endereco'),
]
