from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def sign_up(request):
    """Contains the user registration form"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # # Check if all fields are provided
        # if not email or not username or not phone or not password or not confirm_password:
        #     messages.error(request, "Please fill all the fields!")
        #     return render(request, "auth/sign_up.html")

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('user_auth:login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exists")
        else:
            # Display a message saying passwords dont match
            messages.error(request, "Passwords do not match!")
            
    return render(request, "auth/sign_up.html")

def sign_in(request):
    """Contains the user login form"""
    # Check if its a POST method
    if request.method == 'POST':
        # Add the input fields
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        # Check if the user exists
        if user is not None:
            login(request, user)
            messages.success(request, "Login success!")
            return redirect('telemed_app:home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "auth/sign_up.html")

def user_logout(request):
    """Function to logout"""
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('user_auth:home')
