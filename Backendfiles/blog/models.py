from django.db import models
from django.db.models import Count

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
    title = models.CharField(max_length=127,)
    author = models.CharField(max_length=127, default='Admin')
    author_about = models.TextField(max_length=500, default='')
    author_position = models.CharField(max_length=127, )
    author_image = models.ImageField(upload_to = 'blog-author-image/')
    blog_date = models.DateField(auto_now=True)
    blog_text1 = models.TextField(max_length=500, default='')
    blog_text2 = models.TextField(max_length=500, default='') 
    blog_text3 = models.TextField(max_length=500, default='')
    title_2 = models.CharField(max_length=127, default='')
    blog_text4 = models.TextField(max_length=500, default='')
    blog_text5 = models.TextField(max_length=500, default='')
    

    class Meta:
        ordering = ['-blog_date']
        verbose_name = 'blog_Post'
    
    def __str__(self):

        return f'{self.title, self.blog_date}'
    

class Comment(models.Model):
    STATUS_CHOICES = (
        ('reject', 'Reject'),
        ('approve', 'Approve'),
    )

    blog =  models.ForeignKey(blog_Post, on_delete=models.CASCADE, related_name='show_all_comments')
    letter = models.TextField(blank= False, null= False)
    name = models.CharField(max_length=100, blank= False, null= False)
    email = models.EmailField(blank=False, null=False)
    image = models.ImageField(upload_to = 'comment-image/')
    date_add = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='reject')
    

    class Meta:
        ordering = ['-date_add']

    def __str__(self):
        return f'Comment {self.letter} by {self.name}'
    
    @property
    def comment_count(self):
        return self.letter.count()


class commenter(models.Model):
    blog =  models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='show_commentters')
    name = models.CharField(max_length=100, default='')
    

    class Meta:
        ordering = ['name']
    

    def __str__(self):
        return f'Comment {self.blog} by {self.name}'

    

    
    
