from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from userposts.models import userpost
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login_auth(request, user)
            messages.success(request, 'Sucessfully logged in.')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid Username and Password.')
            return redirect('login')
    return render(request, 'login/login.html')

def logout(request):
    if request.method == "GET":
        messages.success(request, "Sucessfully logged out.")
        logout_auth(request)
        return render(request, 'appleStarts/homepage.html')
    return render(request, 'appleStarts/homepage.html')