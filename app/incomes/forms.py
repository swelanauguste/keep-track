from django import forms

from .models import Income


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["account", "category", "amount", "description", "transaction_date"]
