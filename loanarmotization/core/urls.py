from django.urls import path
from . import views
from .views import Loans


urlpatterns = [
    path('',Loans.as_view(),name='loan'),
    path('createloan/',views.createLoan, name='createloan')

]