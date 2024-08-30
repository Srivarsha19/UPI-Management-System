from django.db import models
from django.contrib.auth.models import User

class UPIAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upi_id = models.CharField(max_length=255, unique=True)
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.upi_id

class Transaction(models.Model):
    upi_account = models.ForeignKey(UPIAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.upi_account.upi_id} - {self.amount}"
