from rest_framework import serializers
from ..models.transaction import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = Transaction
        fields = ["id", "user", "user_email", "text", "amount", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "user_email", "created_at", "updated_at"]
    
    def create(self, validated_data):
        """Associe automatiquement l'utilisateur connecté à la transaction"""
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)