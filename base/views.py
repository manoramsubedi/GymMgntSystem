from django.shortcuts import render
from .models import Banners, Service, Page

# Create your views here.

def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3]
    context = {'banners':banners, 'services':services}
    return render(request, 'base/home.html', context)

def page_detail(request, id):
    page = Page.objects.get(id=id)
    context = {'page':page}
    return render(request, 'base/page.html', context)

