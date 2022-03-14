from re import template
from django.shortcuts import render
from django.http import HttpResponse
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

    if request.method == 'POST':
        comment = Comment()
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.POST.get('image')
        letter = request.POST.get('letter')
        
        comment.name = name
        comment.email = email
        comment.letter = letter
        comment.image = image
        comment.blog = blog
        comment.save()
        
        return  render (request, 'single-post.html', {'blog':blog})
        

    new_comment = Comment.objects.filter(status='approve')
    
    return render (request, 'single-post.html', {'blog':blog, 'comment': new_comment})