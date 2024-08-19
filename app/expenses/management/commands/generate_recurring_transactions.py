import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from ...models import Expense, RecurringTransaction


class Command(BaseCommand):
    help = "Generate transactions for recurring expenses"

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        recurring_transactions = RecurringTransaction.objects.filter(
            next_occurrence__lte=today
        )

        for rt in recurring_transactions:
            Expense.objects.create(
                user=rt.user,
                account=rt.account,
                category=rt.category,
                amount=rt.amount,
                description=rt.description,
                transaction_date=timezone.now(),
                transaction_type="expense",
            )

            # Update the next_occurrence date
            if rt.interval == "daily":
                rt.next_occurrence += datetime.timedelta(days=1)
            elif rt.interval == "weekly":
                rt.next_occurrence += datetime.timedelta(weeks=1)
            elif rt.interval == "monthly":
                rt.next_occurrence = rt.next_occurrence.replace(
                    month=(
                        rt.next_occurrence.month + 1
                        if rt.next_occurrence.month < 12
                        else 1
                    ),
                    year=(
                        rt.next_occurrence.year
                        if rt.next_occurrence.month < 12
                        else rt.next_occurrence.year + 1
                    ),
                )
            rt.save()
