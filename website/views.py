from django.shortcuts import render
from .models import *


def index(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        print(contact_name)
    home_page_services = Services.objects.filter(is_home_page=True)
    context = {
        'home_page_services': home_page_services,
    }
    return render(request, 'website/index.html', context)

