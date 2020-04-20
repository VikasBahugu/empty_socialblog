from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from . models import userpost

# Create your views here.
def userposting(request):
    messages.success(request, 'Post successfully created.')

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        photo = request.FILES['postedphotos']
        user_post = userpost(title=title, content=content,photo=photo)
        user_post.save()
        visible = 'visible_posts'
        context = {
           'userkeposts': [userpost.objects.all()]
        }
        # return HttpResponseRedirect("homepage/")
        return redirect('homepage')
    # return HttpResponseRedirect('appleStarts/homepage.html')
    # return render(request, 'appleStarts/homepage.html', context)