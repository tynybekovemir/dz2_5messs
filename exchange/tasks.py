
from celery import shared_task
from django.utils import timezone
from .models import UserProfile,models
from datetime import timedelta
from datetime import datetime

@shared_task
def monthly_coin_reward():
    users = UserProfile.objects.all()
    for user in users:
        user.coin_balance += 100 
        user.save()

@shared_task        
def monthly_coin_reward():
    users = UserProfile.objects.all()
    current_date = timezone.now().date()

    for user in users:
        user.coin_balance += 100
        user.last_burn_date = current_date
        user.save()

@shared_task
def monthly_coin_burn():
    users = UserProfile.objects.filter(last_burn_date__lt=timezone.now() - timedelta(days=30))

    for user in users:
        user.coin_balance = max(0, user.coin_balance - 50)
        user.save()

    def award_coins():
        UserProfile.objects.all().update(balance=models.F('balance') + 100)
@shared_task
def burn_coins():
    UserProfile.objects.all().update(balance=models.F('balance') - 50)