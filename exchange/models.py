from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)

class Transaction(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coin_balance = models.IntegerField(default=0)
    last_burn_date = models.DateField(null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username