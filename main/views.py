from django.shortcuts import render
from . import models


def index(request):
    baners = models.Baner.objects.all()
    services = models.Service.objects.all()
    contact = models.Contact.objects.all()
    context = {
        'baners':baners,
        'services':services,
        'contact':contact
    }

    return render(request, 'index.html', context)