# models.py
from django.db import models
from django.contrib.auth.models import User

class Contribution(models.Model):
    CONTRIBUTION_TYPE = [
        ('daily', 'Daily'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=CONTRIBUTION_TYPE)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"
