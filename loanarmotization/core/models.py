from django.db import models

# Create your models here.
class Loan(models.Model):
    principal = models.DecimalField(max_digits=10,decimal_places=2)
    interest_rate = models.FloatField()
    duration_months = models.PositiveIntegerField()
    issue_date = models.DateField()
