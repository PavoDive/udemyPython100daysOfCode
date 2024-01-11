from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Product, Cart
from django.contrib.auth.decorators import login_required  # Import this decorator
from django.conf import settings
from django.contrib import messages
import stripe
import json

# Create your views here.

def index(request):
    products_list = Product.objects.all()
    template = loader.get_template("products/index.html")
    context = {"products_list": products_list}
    # with HttpResponse
    # return HttpResponse(template.render(context, request))
    # with shortcuts.render
    return render(request, "products/index2.html", context)
    
def product(request, product_id):
    product_to_display = get_object_or_404(Product, pk=product_id)
    context = {"product": product_to_display}
    return render(request, "products/product_detail.html", context)

def display_cart(request):
    user_cart = Cart.objects.filter(user=request.user)
    context = {'user_cart': user_cart}
    return render(request, 'products/display_cart.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user, ordered_products = product)
    
    # If the product is already in the cart, increase the quantity
    if not created:
        user_cart.quantity += 1
        user_cart.save()

    return redirect('display_cart')

def remove_from_cart(request, cart_id):
    cart_entry = get_object_or_404(Cart, pk=cart_id)
    cart_entry.delete()
    return redirect('display_cart')

def checkout(request):
    user_cart = Cart.objects.filter(user=request.user)
    total_amount = sum(cart_entry.ordered_products.product_price * cart_entry.quantity for cart_entry in user_cart)
    context = {'user_cart': user_cart, 'total_amount': total_amount}
    return render(request, 'products/checkout.html', context)

def process_order(request):
    if request.method == 'POST':
        # Process the order and handle the payment with Stripe
        # Update the order status, create a delivery file, etc.

        messages.success(request, 'Payment successful. Your order will be processed.')

        # Clear the user's shopping cart
        user_cart = Cart.objects.filter(user=request.user)
        order_id = user_cart[0].id
        order_user = user_cart[0].user.username

        order_items = [{"item": cart_entry.ordered_products.product_name, "qty": cart_entry.quantity} for cart_entry in user_cart]
        order_summary = {"id": order_id, "user": order_user, "items": order_items}
        with open("orders.txt", "a") as f:
            f.write(json.dumps(order_summary))
            f.write("\n")
        
        user_cart.delete()

        return redirect('index')
    else:
        return redirect('checkout')
