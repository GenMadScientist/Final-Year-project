# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('daily/', views.daily_contributions, name='daily_contributions'),
    path('monthly/', views.monthly_contributions, name='monthly_contributions'),
    path('yearly/', views.yearly_contributions, name='yearly_contributions'),
]
