from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
       
        if User.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect('register')
        else:
            user = User(email=email,  password=password)
            user.save()
            print('user created')
            return redirect('/')
    else:
        return render(request, "register.html")