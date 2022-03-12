from email.mime import image
from email.policy import default
from django.db import models

# Create your models here.

class about_Post(models.Model):
    about_name = models.CharField(max_length=127, blank = False, null = False)
    about_title = models.TextField(max_length=127, blank = False, null = False)
    image = models.ImageField(upload_to = 'about_post/', default='')
    about_who = models.CharField(max_length=100, blank = False, null = False)
    about_text1 = models.TextField(max_length=200, blank = False, null = False)
    about_text2 = models.TextField(max_length=300, blank = False, null = False)
    about_text3 = models.TextField(max_length=300, blank = False, null = False)
    about_text4 = models.TextField(max_length=300, blank = False, null = False)

    class Meta:
        verbose_name = 'about_Post'
        verbose_name_plural = 'about_Posts'

    def __str__(self):
        return f'{self.about_name}, {self.about_who}'


class about_work(models.Model):
    work_name = models.CharField(max_length=50, blank = False, null = False)
    work_subtitle_1 = models.CharField(max_length=50, blank = False, null = False)
    work_subtitle_2 = models.CharField(max_length=50, blank = False, null = False)
    work_subtitle_3 = models.CharField(max_length=50, blank = True, null = True)
    work_subtitle_4 = models.CharField(max_length=50, blank = True, default='')

    class Meta:
        verbose_name = 'about_work'
        verbose_name_plural = 'about_works'

    def __str__(self):
        return f'{self.work_name}'