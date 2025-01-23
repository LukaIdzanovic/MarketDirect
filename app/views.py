

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context={}
    return render(request, 'app/home.html', context)

def add_product(request):
    if request.accounts.is_authenticated and request.accounts.vendor:
        pass

def remove_product(request):
    if request.accounts.is_authenticated and request.accounts.vendor:
        pass

def profile(request):
    accounts=request.user,
    

    context = {
        'username': request.user.username,
        'first_name':request.user.first_name ,
        'last_name':request.user.last_name,
        'email':request.user.email,
        
        
    }
    return render(request, 'app/profile.html', context)
