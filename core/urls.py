from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('loan-list/', views.loan_list, name='loan_list'),
    path('create/', views.createLoan, name='create_loan'),
    path('success/', views.loan_success, name='loan_success'),
    path('schedule/<int:loan_id>/', views.loan_schedule, name='loan_schedule')

]