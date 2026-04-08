from django.shortcuts import render, redirect
from .models import Product


# HOME → SHOW DRAMAS
def home(request):
    return render(request, 'home.html')


# CATEGORY → PRODUCTS
def category_view(request, drama_name):
    print("URL drama:", drama_name)  # debug

    products = Product.objects.filter(drama_name=drama_name)

    print("Products found:", products)  # debug

    return render(request, 'category.html', {
        'products': products,
        'category_name': drama_name
    })

# PRODUCT DETAIL
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


# CART
# ADD TO CART
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('/cart/')


# INCREASE QUANTITY
def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1

    request.session['cart'] = cart
    return redirect('/cart/')


# DECREASE QUANTITY
def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] -= 1

        if cart[str(product_id)] <= 0:
            del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('/cart/')


# CART VIEW
def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    total = 0
    cart_items = []

    for product in products:
        qty = cart[str(product.id)]
        total += product.price * qty

        cart_items.append({
            'product': product,
            'quantity': qty
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        qty = cart[str(product.id)]
        total += product.price * qty

        cart_items.append({
            'product': product,
            'quantity': qty
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('/cart/')


# WISHLIST
def add_to_wishlist(request, product_id):
    wishlist = request.session.get('wishlist', [])

    if product_id not in wishlist:
        wishlist.append(product_id)

    request.session['wishlist'] = wishlist
    return redirect('/wishlist/')


def wishlist_view(request):
    wishlist = request.session.get('wishlist', [])
    products = Product.objects.filter(id__in=wishlist)

    return render(request, 'wishlist.html', {'products': products})


def remove_from_wishlist(request, product_id):
    wishlist = request.session.get('wishlist', [])

    if product_id in wishlist:
        wishlist.remove(product_id)

    request.session['wishlist'] = wishlist
    return redirect('/wishlist/')

def checkout(request):
    return render(request, 'checkout.html')