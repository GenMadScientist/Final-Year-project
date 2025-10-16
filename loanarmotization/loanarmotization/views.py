from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def homepage(request):
    #return HttpResponse("This is the homepage")
    return render(request,"home.html")

def aboutuspage(request):
    return render(request,"about.html")

def contactuspage(request):
    return render(request,"contact-us.html")

def pricingpage(request):
    return render(request,"pricing.html")

def servicespage(request):
    return render(request,"services.html")