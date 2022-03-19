from django.shortcuts import render, redirect
from contact.models import Contact
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            detail = request.POST.get('detail'),

        )
        return redirect ('index/')

    return render (request, 'contact.html')