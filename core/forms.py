from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['loan_amount', 'interest_rate', 'duration_months', 'purpose']
        widgets = {
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter loan amount'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Interest rate (%)'}),
            'duration_months': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration (months)'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Purpose of loan'}),
        }
