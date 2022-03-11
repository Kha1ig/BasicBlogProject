from django.shortcuts import render
from index.models import index_Post

# Create your views here.

def index(request):

    indexs = index_Post.objects.all()

    context = {
        'index': indexs
    }

    return render (request, 'index.html', context = context)

def index_detail(request,pk):

    new_index = index_Post.objects.get(pk=pk)

    return render (request, 'single-project.html', {'index': new_index})