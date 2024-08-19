from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import IncomeForm
from .models import Income


@login_required
def add_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect("account_detail", account_id=income.account.id)
    else:
        form = IncomeForm()
    return render(request, "incomes/add_income.html", {"form": form})
