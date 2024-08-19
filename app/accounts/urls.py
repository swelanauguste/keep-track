from django.urls import path

from .views import account_detail, account_list, add_account

urlpatterns = [
    path("", account_list, name="account_list"),
    path("account/add", add_account, name="add_account"),
    path("account/detail/<int:pk>/", account_detail, name="account_detail"),
    # Add other URLs here...
]
