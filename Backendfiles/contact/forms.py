from django import forms
from .models import Contact

# 

class Meta(forms.ModelForm):
    model = Contact
    fields = '__all__'