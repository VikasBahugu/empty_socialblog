from django.shortcuts import render, HttpResponse, redirect
from . models import signup
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def sign(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        number = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        nam = len(name)
        numbe = len(number)

        context = {'details': [nam,email,username,numbe,password1,password2]}
        if nam < 2 or '@' not in email or password1 != password2 or numbe<10:
            return render(request, 'signup/signup.html', context)

        else:
            flag=1
            # letters = [0,1,2,3,4,5,6,7,8,9] #######Add letters for strong password.
            context = {'details': [name, flag]}
            new_user = User.objects.create_user(username, email, password1)
            # if ' ' in name:
            #     fname, lname = name.split(' ', 1)
            #     myuser.first_name = fname
            #     myuser.last_name = lname
            # else:
            #     myuser.first_name = name
            new_user.save()
            messages.success(request,"Successfully created user.")
            return redirect('login')


    return render(request, 'signup/signup.html')
