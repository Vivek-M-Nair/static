from django.urls import path
from . import views
urlpatterns=[
    path('summary/',views.summary,name='summary'),
    path('login_reg/',views.login_reg,name='login_reg'),
    path('home/',views.home,name='home'),
]