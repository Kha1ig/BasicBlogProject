from email.policy import default
from django.db import models

# Create your models here.

class index_Post(models.Model):
    image = models.ImageField(upload_to = 'index_Post/')
    image1 = models.ImageField(upload_to = 'index_Post_detail/', default = '')
    image2 = models.ImageField(upload_to = 'index_Post_detail/', default = '')
    image3 = models.ImageField(upload_to = 'index_Post_detail/', default = '')
    post_name = models.CharField(max_length=20, blank = False, null = False, default='Project Name')
    post_type = models.CharField(max_length=20, blank = False, null = False, default='Null')
    post_title = models.CharField(max_length=127, blank = False, null = False, default='Null')
    post_date = models.DateTimeField(auto_now=True)
    post_client = models.CharField(max_length=20, default='Admin')
    post_text = models.TextField(max_length=300, blank = False, null = False, default='Null')
    post_manager = models.CharField(max_length=50, blank = False, null = False, default='Admin')


    class Meta:
        verbose_name = 'index_Post'
        verbose_name_plural = 'index_Posts'

    def __str__(self):
        return f'{self.image}, {self.post_date}'
