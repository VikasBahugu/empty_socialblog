from django.shortcuts import render, HttpResponse, redirect
from . models import ContactUS
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['reason']
        nam = len(name)
        conten = len(content)
        context = {'flag': [nam, email, conten]}

        if nam < 2 or '@gmail.com' not in email or conten < 4:
            for_invalid = 'valid_contact_info'
            context = {'flag': [nam, email, conten, for_invalid]}
            return render(request, 'contact/used_contact.html', context)
        elif nam > 2 and '@gmail.com' in email and conten > 4:
            contact_user = ContactUS(name=name, email=email, content=content)
            contact_user.save()
            flag = 1
            context = {'flag': [name, email, conten, flag]}
            # return render(request, 'appleStarts/homepage.html', context)
            messages.success(request, 'Thanks for contacting us, we will reach out to you shortly.')
            return redirect("homepage")

    return render(request, 'contact/used_contact.html')