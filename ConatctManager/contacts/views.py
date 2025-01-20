from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Contacts
from django.http import HttpResponse # type: ignore
from django.db import models # type: ignore

# Create your views here.
def contact_list(request):
    #contacts = Contacts.objects.all() #fetching all the contacts
    query = request.GET.get('query', '')
    contacts = Contacts.objects.filter(
        models.Q(name__icontains=query) | models.Q(email__icontains=query)
    )
    return render(request,'contacts/contact_list.html',{'contacts':contacts,'query': query})

def contact_detail(request,pk):
    contact = get_object_or_404(Contacts,pk=pk)
    return render(request,'contacts/contact_detail.html',{'contact': contact})

def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name') #Getting and storing the data from HTML Varibale in views vairable
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Contacts.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('contact_list')
    return render(request, 'contacts/add_contact.html')
