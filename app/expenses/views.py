from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ExpenseForm
from .models import Expense


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("account_detail", account_id=expense.account.id)
    else:
        form = ExpenseForm()
    return render(request, "expenses/add_expense.html", {"form": form})
