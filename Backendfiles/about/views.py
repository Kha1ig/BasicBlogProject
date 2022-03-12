import imp
from django.shortcuts import render
from about.models import about_Post, about_work

# Create your views here.

def about(request):

    abouts = about_Post.objects.all()
    about2 = about_work.objects.all()

    context = {
        'about': abouts,
        'about3': about2
    }


    
    return render (request, 'about.html', context = context  )

