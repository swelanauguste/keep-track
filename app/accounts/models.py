from django.db import models
from django.utils import timezone
from users.models import User


class Account(models.Model):
    CHECKING = "checking"
    SAVINGS = "savings"
    CREDIT = "credit"
    ACCOUNT_TYPES = [
        (CHECKING, "Checking"),
        (SAVINGS, "Savings"),
        (CREDIT, "Credit"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.CharField(
        max_length=10, choices=ACCOUNT_TYPES, default=CHECKING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    currency = models.CharField(max_length=10, default="XCD")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()}) - {self.balance} {self.currency}"
