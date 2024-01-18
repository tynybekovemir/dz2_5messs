from rest_framework import serializers
from .models import UserProfile, Transaction

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'balance')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('sender', 'receiver', 'amount', 'timestamp')