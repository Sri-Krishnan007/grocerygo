from django.shortcuts import render,get_object_or_404, redirect
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
import random
from .models import Product, Category,Cart,Order,UserProfile
from .forms import OrderForm
from decimal import Decimal
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
def main_page(request):
    return render(request, 'main/main_page.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                # Create user
                user = User.objects.create_user(username=email, email=email, password=password)

                # Create UserProfile
                UserProfile.objects.create(user=user, phone_number=phone, email=email)

                # Generate email verification token (implement token generation logic)
                verification_link = f'http://localhost:8000/login/'  # Update this with your actual verification link logic
                
                # Send verification email
                send_mail(
                    'Verify your email',
                    f'Click the link to verify: {verification_link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Signup successful! Check your email for verification.')
                return redirect('signup')  # Redirect back to the signup page
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'main/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Generate and send OTP
            otp = random.randint(1000, 9999)
            send_mail(
                'Your OTP',
                f'Your OTP is {otp}',
                'srikrish2705guru@gmail.com',
                [email],
                fail_silently=False,
            )
            # Store OTP temporarily (can be implemented with session)
            request.session['otp'] = otp
            return redirect('otp_verification')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'main/login.html')


def otp_verification_view(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if otp == str(request.session['otp']):
            messages.success(request, 'Login Successful')
            return redirect('product_list')  # Redirect to product list page
        else:
            messages.error(request, 'Invalid OTP')
    return render(request, 'main/otp_verification.html')
def product_list(request):
    
    # Fetch all categories
    categories = Category.objects.all()

    # Get the selected category and search query from request parameters
    selected_category = request.GET.get('category', 'all')
    search_query = request.GET.get('query', '')

    # Filter products based on the selected category
    if selected_category and selected_category != 'all':
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.all()  # Show all products if no category is selected

    # Further filter products based on the search query
    if search_query:
        products = products.filter(name__icontains=search_query)

    # Prefetch the UserProfile to avoid additional database hits
    user_profile = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
        'search_query': search_query,
        'user_profile': user_profile  # Pass the user profile to the template if needed
    }
    return render(request, 'main/product_list.html', context)
# Product detail view
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'main/product_detail.html', {'product': product})


@login_required
def checkout(request):
    if request.method == 'POST':
        # Assuming cart is stored in session and contains product IDs and quantities
        cart = request.session.get('cart', {})
        shipping_address = request.POST.get('shipping_address')
        email = request.POST.get('email')
        
        # Loop through the cart and create an order for each product
        for product_id, item in cart.items():
            product = Product.objects.get(id=product_id)
            quantity = item['quantity']
            total_price = product.price * quantity

            # Create and save the order
            order = Order.objects.create(
                product=product,
                quantity=quantity,
                customer_name=request.user.username,  # Assuming the logged-in user is the customer
                shipping_address=shipping_address,
                order_status='pending',  # Set initial status to pending
                total_price=total_price,
                payment_status='pending'  # Cash on delivery
            )

            # Send a confirmation email to the user input email address
            send_mail(
                subject='Order Confirmation - GroceryGO',
                message=f'Thank you for your order! Your order #{order.id} will be delivered in 1 hour. Cash on delivery.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],  # Send to user-provided email
                fail_silently=False,
            )

        # Clear the cart after order placement
        request.session['cart'] = {}

        # Display a success message (optional)
        return render(request, 'main/checkout_success.html', {'message': 'Your order has been placed! It will be delivered in 1 hour.'})

    return render(request, 'main/checkout.html')

# Order history
def order_history(request):
    customer_name = request.user.username  # Assuming customer_name matches the logged-in user's username
    orders = Order.objects.filter(customer_name=customer_name)  # Filter by customer_name

    return render(request, 'main/order_history.html', {'orders': orders})



from django.shortcuts import render, get_object_or_404
from .models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    # Get the cart from the session or initialize a new cart
    cart = request.session.get('cart', {})

    # Convert price from Decimal to float to avoid JSON serialization issues
    product_price = float(product.price)

    # If the product is already in the cart, update the quantity
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
    else:
        # Add the product to the cart
        cart[str(product_id)] = {
            'name': product.name,
            'price': product_price,  # Store price as float
            'quantity': quantity,
        }
    
    # Save the cart back to the session
    request.session['cart'] = cart

    # Prepare a success message
    message = f"{product.name} was added to your cart."

    # Render the same page with the success message
    return render(request, 'main/product_detail.html', {'product': product, 'message': message})

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_with_totals = {}
    total = 0

    # Multiply the price by quantity in the view
    for product_id, item in cart.items():
        subtotal = item['price'] * item['quantity']
        cart_with_totals[product_id] = {
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'subtotal': subtotal
        }
        total += subtotal

    return render(request, 'main/cart.html', {'cart': cart_with_totals, 'total': total})


def checkout_success(request):
    return render(request, 'main/checkout_success.html')

