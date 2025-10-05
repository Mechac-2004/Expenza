from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers.transaction import TransactionSerializer
from ..models.transaction import Transaction

class TransactionListCreateView(generics.ListCreateAPIView):
    """
    API endpoint pour lister toutes les transactions et créer une nouvelle transaction.
    
    GET: Retourne la liste de toutes les transactions de l'utilisateur connecté
    POST: Crée une nouvelle transaction pour l'utilisateur connecté
    """
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Retourne uniquement les transactions de l'utilisateur connecté"""
        return Transaction.objects.filter(user=self.request.user)
    
    @swagger_auto_schema(
        operation_description="Récupère la liste de toutes les transactions",
        responses={200: TransactionSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Crée une nouvelle transaction",
        request_body=TransactionSerializer,
        responses={
            201: TransactionSerializer(),
            400: "Données invalides"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint pour récupérer, modifier ou supprimer une transaction spécifique.
    
    GET: Retourne les détails d'une transaction
    PUT/PATCH: Met à jour une transaction
    DELETE: Supprime une transaction
    """
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    
    def get_queryset(self):
        """Retourne uniquement les transactions de l'utilisateur connecté"""
        return Transaction.objects.filter(user=self.request.user)
    
    @swagger_auto_schema(
        operation_description="Récupère les détails d'une transaction spécifique",
        responses={
            200: TransactionSerializer(),
            404: "Transaction non trouvée"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Met à jour complètement une transaction",
        request_body=TransactionSerializer,
        responses={
            200: TransactionSerializer(),
            400: "Données invalides",
            404: "Transaction non trouvée"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Met à jour partiellement une transaction",
        request_body=TransactionSerializer,
        responses={
            200: TransactionSerializer(),
            400: "Données invalides",
            404: "Transaction non trouvée"
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Supprime une transaction",
        responses={
            204: "Transaction supprimée avec succès",
            404: "Transaction non trouvée"
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)