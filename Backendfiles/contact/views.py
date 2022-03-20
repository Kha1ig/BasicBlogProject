from django.shortcuts import render, redirect
from contact.models import Contact
from contact.forms import ContactForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def contact(request):

    forum = ContactForm()
    if request.method == 'POST':
        forum = ContactForm(data=request.POST)
        if forum.is_valid():
            forum.save()
            return redirect(reverse('index:index'))

    return render (request, 'contact.html', {'forum': forum})
