# views.py
from django.shortcuts import render
from .models import Contribution
from django.contrib.auth.decorators import login_required

@login_required
def daily_contributions(request):
    contributions = Contribution.objects.filter(type='daily', user=request.user)
    return render(request, 'contributions/daily_contributions.html', {'contributions': contributions})

@login_required
def monthly_contributions(request):
    contributions = Contribution.objects.filter(type='monthly', user=request.user)
    return render(request, 'contributions/monthly_contributions.html', {'contributions': contributions})

@login_required
def yearly_contributions(request):
    contributions = Contribution.objects.filter(type='yearly', user=request.user)
    return render(request, 'contributions/yearly_contributions.html', {'contributions': contributions})
