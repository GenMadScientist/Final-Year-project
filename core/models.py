from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Loan(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2, default=10000)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Interest rate in percentage")
    duration_months = models.PositiveIntegerField(help_text="Loan duration in months")
    date_created = models.DateTimeField(default=date.today)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ])
    def __str__(self):
        return f"{self.borrower.username} - {self.loan_amount} ({self.status})"

    def monthly_payment(self):
        """Calculate monthly payment using amortization formula"""
        P = float(self.loan_amount)
        r = float(self.interest_rate) / 100 / 12
        n = int(self.duration_months)

        if r == 0:
            return P / n
        payment = P * (r * pow(1 + r, n)) / (pow(1 + r, n) - 1)
        return round(payment, 2)

    def amortization_schedule(self):
        """Return a list of dicts with payment details"""
        schedule = []
        balance = float(self.loan_amount)
        r = float(self.interest_rate) / 100 / 12
        n = int(self.duration_months)
        monthly_payment = self.monthly_payment()

        for month in range(1, n + 1):
            interest = balance * r
            principal = monthly_payment - interest
            balance -= principal
            schedule.append({
                'month': month,
                'payment': round(monthly_payment, 2),
                'principal': round(principal, 2),
                'interest': round(interest, 2),
                'balance': round(abs(balance), 2)
            })
        return schedule