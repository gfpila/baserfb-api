from django.contrib import admin
from django.urls import path, include
from .views import EstabelecimentosListView

from . import views

urlpatterns = [
    path('estabelecimentos/', EstabelecimentosListView.as_view(), name='estabelecimentos'),
]