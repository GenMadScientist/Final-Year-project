from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from core.forms import LoanForm
from django.contrib.auth.models import User
from core.models import Loan
# Create your views here.

def homepage(request):
    #return HttpResponse("This is the homepage")
    return render(request,"core/home.html")

login_required
def loan_list(request):
    loans = Loan.objects.filter(borrower=request.user).order_by('-date_created')
    latest_loan = loans.first()  # Get the newest loan or None
    return render(request, 'core/loan_list.html', {'loans': loans, 'latest_loan': latest_loan})

def createLoan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.borrower = request.user
            loan.save()
            return redirect('loan_schedule', loan_id=loan.id)
    else:
        form = LoanForm()
    return render(request, 'core/create_loan.html', {'form': form})

def loan_success(request):
    return render(request, 'core/loan_success.html')

@login_required
def loan_schedule(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, borrower=request.user)
    schedule = loan.amortization_schedule()
    return render(request, 'core/loan_schedule.html', {'loan': loan, 'schedule': schedule})
