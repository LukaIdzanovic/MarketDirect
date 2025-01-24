
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Account


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
    user = request.user 

    if not user.is_authenticated:
        return render(request, 'registration/login.html')
    
    try:
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        account = None

    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'balance': account.balance
    }
    return render(request, 'app/profile.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'app/products.html', context)


def shops(request):
    vendors = Account.objects.filter(vendor=True)

    context = {
        'vendors': vendors,
    }
    return render(request, 'app/shops.html', context)