from django.shortcuts import render, redirect
from account.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            try:
                print('user is:')
                print(user.labors.post)
                print('this')
                if user.labors.post == 'labor':
                    return redirect('labor:dashboard')
                if user.labors.post == 'supervisor':
                    return redirect('supervisor:dashboard')
                if user.labors.post == 'ceo':
                    return redirect('ceo:dashboard')
            except Exception as e:
                return redirect('recruitment:dashboard')
        else:

            messages.error(request, 'invalid credentials')
            redirect('account:login')
    return render(request, 'account/login.html')
def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(email, password, confirm_password)
        if password != confirm_password:
            messages.error(request, 'password and confrim password does not match!')
            return render(request, 'account/signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'account/signup.html')
        user = User.objects.create(email=email, password=make_password(password))
        user.save()
        messages.success(request, 'User registered successfully!')
        return redirect('account:login')
    else:
        return render(request, 'account/signup.html')

def logout_view(request):
    logout(request)
    return redirect ('account:login')