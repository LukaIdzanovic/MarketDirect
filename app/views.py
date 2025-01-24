
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Product, Account, Cart, CartItem
from django.db import transaction
from django.contrib import messages


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
def shop_detail(request, shop_id):
    try:
        # Dohvat vendora prema ID-u
        vendor = Account.objects.get(id=shop_id, vendor=True)
        # Dohvat svih proizvoda tog vendora
        products = Product.objects.filter(user=vendor.user)

        context = {
            'vendor': vendor,
            'products': products,
        }
        return render(request, 'app/shop_detail.html', context)
    except Account.DoesNotExist:
        return redirect('shops') 

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


from django.shortcuts import get_object_or_404

@login_required
def cart(request):
    # Dohvat košarice korisnika
    cart, created = Cart.objects.get_or_create(user=request.user)

    context = {
        'cart': cart,
        'items': cart.items.all(),  # Sve stavke u košarici
        'total': cart.total
    }
    return render(request, 'app/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    # Dohvat proizvoda
    product = get_object_or_404(Product, id=product_id)

    # Dohvat ili stvaranje korisnikove košarice
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Provjera postoji li proizvod već u košarici
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        # Ako stavka već postoji, povećaj količinu
        cart_item.quantity += 1
    cart_item.save()

    # Ažuriraj ukupan iznos košarice
    cart.total = sum(item.subtotal for item in cart.items.all())
    cart.save()

    return redirect('cart')  # Preusmjeri na prikaz košarice

@login_required
def remove_from_cart(request, item_id):
    # Dohvat stavke u košarici
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart = cart_item.cart

    # Uklanjanje stavke
    cart_item.delete()

    # Ažuriraj ukupan iznos košarice
    cart.total = sum(item.subtotal for item in cart.items.all())
    cart.save()

    return redirect('cart')


@login_required
def checkout(request):
    try:
        # Dohvaćanje košarice korisnika
        cart = Cart.objects.get(user=request.user)
        
        if cart.total > request.user.account.balance:
            # Provjera je li kupac ima dovoljno novca
            messages.error(request, "Nemate dovoljno sredstava za ovu kupnju.")
            return redirect('cart')

        # Transakcija za osiguranje konzistentnosti podataka
        with transaction.atomic():
            for item in cart.items.all():
                # Dodavanje iznosa na saldo vendora
                vendor_account = item.product.user.account
                vendor_account.balance += item.subtotal
                vendor_account.save()

            # Smanjivanje korisnikovog balansa
            request.user.account.balance -= cart.total
            request.user.account.save()

            # Brisanje stavki iz košarice nakon kupnje
            cart.items.all().delete()
            cart.total = 0
            cart.save()

        messages.success(request, "Kupnja uspješno obavljena!")
        return redirect('cart')

    except Cart.DoesNotExist:
        # Ako korisnik nema košaricu
        messages.error(request, "Vaša košarica je prazna.")
        return redirect('cart')

