from django.forms import ModelForm
from blog.models import Comment
from django import forms

class CommentForm(ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ('letter','name','email', 'image')

        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Name',

                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Email',

                }
            ),
            'image': forms.FileInput(
                
            ),

            'letter': forms.Textarea(
                attrs = {
                'class': 'form-control',
                'rows':   "5",
                'placeholder': 'Message ',
                }
            ),
            
            }
