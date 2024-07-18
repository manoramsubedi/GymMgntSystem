from django.shortcuts import render
from .models import Banners

# Create your views here.

def home(request):
    banners = Banners.objects.all()
    context = {'banners':banners}
    return render(request, 'base/home.html', context)