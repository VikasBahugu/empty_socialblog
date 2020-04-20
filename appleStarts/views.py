from django.shortcuts import render, HttpResponse
from userposts.models import userpost
from django.contrib import messages

# Create your views here.
def homepage(request):
    visible = 'visible_posts'
    context = {
        'userkeposts':[userpost.objects.all(),visible]
    }

    return render(request, 'appleStarts/homepage.html',context)
