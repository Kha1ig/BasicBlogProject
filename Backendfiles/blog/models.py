from email.mime import image
from email.policy import default
from tabnanny import verbose
from turtle import title
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.

class blog_header(models.Model):
    title_1 = models.CharField(max_length=50, blank = False, null = False)
    title_2 = models.TextField(max_length=127, blank = False, null = False)

    class Meta:
        verbose_name = 'blog_header'
    
    def __str__(self):

        return f'{self.title_1}'

class blog_Post(models.Model):
    blog_image = models.ImageField(upload_to = 'blog-post-image/')
    title = models.CharField(max_length=127, blank = False, null = False)
    author = models.CharField(max_length=127, blank = False, null = False, default='Admin')
    author_position = models.CharField(max_length=127, blank = False, null = False, default='Admin')
    author_image = models.ImageField(upload_to = 'blog-author-image/')
    blog_date = models.DateField(auto_now=True)
    blog_text1 = models.TextField(max_length=500, blank = False, null = False, default='')
    blog_text2 = models.TextField(max_length=500, blank = False, null = False, default='') 
    blog_text3 = models.TextField(max_length=500, blank = False, null = False, default='')
    title_2 = models.CharField(max_length=127, blank = False, null = False, default='')
    blog_text4 = models.TextField(max_length=500, blank = False, null = False, default='')
    blog_text5 = models.TextField(max_length=500, blank = False, null = False, default='')

    class Meta:
        verbose_name = 'blog_Post'
    
    def __str__(self):

        return f'{self.title, self.blog_date}'
    

class Comment(models.Model):
    STATUS_CHOICES = (
        ('approve', 'Approve'),
        ('reject', 'Reject'),
    )

    blog =  models.ForeignKey(blog_Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    letter = models.TextField()
    email = models.EmailField(default='')
    image = models.ImageField(upload_to = 'comment-author-image/', default = '')
    date_add = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES)

    def __str__(self):
        return (self.name)
    
    
