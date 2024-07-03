from django.shortcuts import render
from . import models


def index(request):
    baners = models.Baner.objects.all()
    services = models.Service.objects.all()
    contact = models.Contact.objects.all()
    info = models.Informations.objects.last()
    advertising = models.Advertising.objects.all()

    if request.method =='POST':
        f_name = request.POST['f_name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        text = request.POST['service']
        
        
        models.Contact.objects.create(
            f_name = f_name,
            email = email,
            phone_number = phone_number,
            text = text
            
        )
    context = {
        'baners':baners,
        'services':services,
        'contact':contact,
        'info':info,
        'advertising':advertising
    }

    return render(request, 'index.html', context)