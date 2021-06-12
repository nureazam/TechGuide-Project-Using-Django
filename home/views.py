from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page!")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page!")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page!")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, address1=address1, address2=address2, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your massages has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page!")

def website(request):
    return render(request, 'website.html')
    # return HttpResponse("this is services page!")

def game(request):
    return render(request, 'game.html')
    # return HttpResponse("this is services page!")

def apks(request):
    return render(request, 'apks.html')