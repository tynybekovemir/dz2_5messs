from django.shortcuts import render
from rest_framework import generics
from .models import UserProfile, Transaction
from .serializers import UserProfileSerializer, TransactionSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@api_view(['POST'])
def transfer_coins(request):
    sender_id = request.data.get('sender_id')
    recipient_id = request.data.get('recipient_id')
    amount = request.data.get('amount')

    sender = UserProfile.objects.get(user_id=sender_id)
    recipient = UserProfile.objects.get(user_id=recipient_id)

    if sender.coin_balance >= amount:
        sender.coin_balance -= amount
        recipient.coin_balance += amount
        sender.save()
        recipient.save()
        return Response({'message': 'Coins transferred successfully'})
    else:
        return Response({'message': 'Insufficient balance'})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_coins(request):
    sender_profile = request.user.userprofile
    receiver_username = request.data.get('receiver_username')
    amount = request.data.get('amount')
    try:
        receiver_profile = UserProfile.objects.get(user__username=receiver_username)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Получатель не найден.'}, status=400)

    if sender_profile.balance >= amount:
        sender_profile.balance -= amount
        receiver_profile.balance += amount
        sender_profile.save()
        receiver_profile.save()
        return Response({'message': 'Перевод успешно выполнен.'})
    else:
        return Response({'error': 'Недостаточно монет для перевода.'}, status=400)
    
