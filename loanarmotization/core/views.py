from django.shortcuts import render,redirect
from django.views import View
from core.forms import LoanForm
from core.models import Loan
# Create your views here.

class Loans(View):
    def get(self,request):
        loan_list = Loan.objects.all()
        context = {'loan_list':loan_list}
        return render(request,"loan-page.html",context)

def createLoan(request):
        form = LoanForm()
        if request.method == 'POST':
             form = LoanForm(request.POST)
             if form.is_valid():
                  form.save()
                  return redirect('loan')
        context = {'form':form}
        return render(request, "create_loan.html", context)
