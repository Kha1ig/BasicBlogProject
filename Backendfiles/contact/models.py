import email
from django.db import models

# Create your models here.

class Contact(models.Model):
    STATUS_CHOICES = (
        ('Budget Select', 'Budget Select'),
        ('$1200 to $1600', '-$1200 to $1600-'),
        ('$2200 to $2400', '-$2200 to $2400-'),
        ('$2500 to $3800', '-$2500 to $3800-'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    detail = models.TextField(max_length=500)
    budget = models.CharField(max_length=51, choices=STATUS_CHOICES, default=STATUS_CHOICES)

    def __str__(self):
        return self.name
