from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AccountForm
from .models import Account


@login_required
def account_list(request):
    accounts = Account.objects.filter(user=request.user)
    form = AccountForm()
    return render(
        request, "accounts/account_list.html", {"accounts": accounts, "form": form}
    )


@login_required
def add_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            if request.is_ajax():
                return JsonResponse({"success": True})
            return redirect("account_list")
        else:
            if request.is_ajax():
                return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = AccountForm()
    return render(request, "accounts/add_account.html", {"form": form})


@login_required
def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id, user=request.user)
    return render(request, "accounts/account_detail.html", {"account": account})
