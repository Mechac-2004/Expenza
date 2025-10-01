from django.contrib import admin
from django.urls import path
from .views.transaction import TransactionListCreateView, TransactionRetrieveUpdateDestroyView

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view()),
    path('transactions/<uuid:id>/', TransactionRetrieveUpdateDestroyView.as_view()),
]