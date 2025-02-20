from django.shortcuts import render
def summary(request):
    return render(request,'summary.html')
def login_reg(request):
    return render(request,'log_reg.html')
def home(request):
    return render(request,'home.html')
    

# Create your views here.
