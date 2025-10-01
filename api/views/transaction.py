from django.shortcuts import render
from rest_framework import generics
from ..serializers.transaction import TransactionSerializer
from ..models.transaction import Transaction

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
class TransactionRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"