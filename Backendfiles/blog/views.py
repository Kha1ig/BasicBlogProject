from django.shortcuts import render, redirect
from django.urls import reverse
from blog.forms import CommentForm
from blog.models import blog_Post, blog_header, Comment, commenter

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def blog(request):
    blog3 = blog_header.objects.all()
    blogs = blog_Post.objects.all()

    context = {
        'blog': blogs,
        'blog2': blog3
    }

    return render (request, 'blog.html', context = context)

@csrf_exempt
def blog_detail(request,pk):
    #new_blog = blog_Post.objects.get(pk=pk)
    blog = blog_Post.objects.filter(pk=pk).first()
    
    new_comment = Comment.objects.filter(status='approve')
    forum = CommentForm()
    if request.method == "POST":
        Comment.objects.create(
            blog=blog_Post.objects.all().filter(pk=pk).first(),
            letter = request.POST.get("letter"),
            name = request.POST.get("name"),
            email = request.POST.get("email"),
            image = request.POST.get("image"),

        )
    

    
    return render (request, 'single-post.html', {'blog':blog, 'forum': forum, 'new_comment': new_comment})
