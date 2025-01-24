
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Product, Account


# Create your views here.
def home(request):
    context={}
    return render(request, 'app/home.html', context)


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

@login_required
def products(request):

    if not request.user.account.vendor:
        return redirect('homepage')

    products = Product.objects.filter(user=request.user)
    context = {
        'products':products,
    }
    return render(request, 'app/products.html', context)

@login_required
def shops(request):

    vendors = Account.objects.filter(vendor=True)

    context = {
        'vendors': vendors,
    }
    return render(request, 'app/shops.html', context)

@login_required
def add_new_products(request):
    if request.user.account.vendor:  # Provjera da li korisnik NIJE vendor
        if request.method == "POST":

            title = request.POST.get('title')
            image = request.POST.get('image')
            description = request.POST.get('description')
            price = request.POST.get('price')

            if title and image and description and price:
                product = Product(
                    title = title,
                    image = image,
                    description = description,
                    price = price,
                    user = request.user
                )
                product.save()
                return redirect( reverse('products'))   
        context = {}
        return render(request, 'app/addNewProduct.html', context)
    return redirect('/')

@login_required
def remove_product(request, product_id):
    if request.user.account.vendor: 
        try:
            product = Product.objects.get(id=product_id, user=request.user)  # Provjera vlasništva
            product.delete()
            return redirect(reverse('products'))
        except Product.DoesNotExist:
            return redirect(reverse('products'))  # Ako proizvod ne postoji
    return redirect('/')


