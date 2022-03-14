from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        detail = request.POST.get('detail')
        budget_select = request.POST.get('budget')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.detail = detail
        contact.budget = budget_select
        contact.save()
        return render (request, 'contact.html')

    return render (request, 'contact.html')