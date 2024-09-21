from django.contrib import admin
from django.urls import path, include
from .views import BankView


urlpatterns = [
    path('', BankView.as_view(), name='bank_view'),
]
