from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def view_appointment(request):
    return render(request, 'view_appointment.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or another page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home page after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'You have successfully signed up! You can now log in.')
                login(request, user)  # Log the user in immediately after signing up
                return redirect('home')  # Redirect to home or another page
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

    return render(request, 'signup.html')

from django.shortcuts import render, redirect
from .models import Appointment

def book_appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        service = request.POST['service']
        date = request.POST['date']
        time = request.POST['time']

        # Save the appointment in the database
        appointment = Appointment(name=name, email=email, phone=phone, service=service, date=date, time=time)
        appointment.save()

        # Redirect to a confirmation page or show success message
        #return redirect('appointment_confirmation')  # You can create an appointment confirmation view and page
    return render(request, 'book_appointment.html')

def facials_services(request):
    return render(request, 'facials_services.html')  # Create a new HTML template for this service

def manicure_pedicure_services(request):
    return render(request, 'manicure_pedicure_services.html')

def hairstyling_services(request):
    return render(request, 'hairstyling_services.html')


def makeup_services(request):
    return render(request, 'makeup_services.html')

from django.shortcuts import render

def body_treatments_services(request):
    return render(request, 'bodytreatments_services.html')  # Ensure the template name is correct


def spa_packages_services(request):
    return render(request, 'spa_packages_services.html')

def moisturizer(request):
    return render(request, 'products/moisturizer.html')

