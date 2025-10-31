from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from core.forms import LoanForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from core.models import Loan
# Create your views here.

def loginPage(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          try:
               user = User.objects.get(username=username)
          except:
               messages.error(request, "User does not exist.")
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request,user)
               return redirect('home')
          else:
               messages.error(request, 'username OR password does not')
     context = {}
     return render(request, 'core/login_register.html', context)

def homepage(request):
    #return HttpResponse("This is the homepage")
    return render(request,"core\home.html")

class Loans(View):
    def get(self,request):
        loan_list = Loan.objects.all()
        context = {'loan_list':loan_list}
        return render(request,"core/loan-page.html",context)

def createLoan(request):
        form = LoanForm()
        if request.method == 'POST':
             form = LoanForm(request.POST)
             if form.is_valid():
                  form.save()
                  return redirect('loan')
        context = {'form':form}
        return render(request, "core/create_loan.html", context)


     
