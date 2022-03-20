from django.forms import ModelForm
from contact.models import Contact
from django import forms
# 

class ContactForm(ModelForm):
    pass

    class Meta:
        model = Contact
        fields = '__all__'

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
            'phone': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Phone Number',

                }
            ),
            'budget': forms.Select(
                attrs = {
                    'class':'form-control',
                    }),
            
            'detail': forms.Textarea(
                attrs = {
                'class': 'form-control',
                'rows':   "5",
                'placeholder': 'Project Details',
                }
            )

        }