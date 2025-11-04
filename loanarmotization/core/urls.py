from django.urls import path
from . import views
from .views import Loans


urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('', views.homepage, name="home"),
    path('loan/',Loans.as_view(),name='loan'),
    path('createloan/',views.createLoan, name='createloan')

]