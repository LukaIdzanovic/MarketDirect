

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.timezone import now



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    vendor = models.BooleanField()

    def __str__(self):
        return f"{self.id} - {self.name}"
    
class Product(models.Model):
    title = models.CharField(max_length=160, null=True, blank=True)
    image = models.CharField(max_length=512)
    description = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.id} -> {self.title}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Svaki korisnik ima svoju košaricu
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Ukupan iznos košarice

    def __str__(self):
        return f"Košarica korisnika {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')  # Pripada kojoj košarici
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Proizvod u košarici
    quantity = models.PositiveIntegerField(default=1)  # Količina proizvoda
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Iznos za ovu stavku

    def save(self, *args, **kwargs):
        # Izračunavanje ukupne cijene stavke
        self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} (Order {self.order.id})"
