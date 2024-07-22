from django.shortcuts import render
from .models import Banners, Service, Page, faq_list, Enquiry
from .forms import EnquiryForm

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

def faq(request):
    faqs = faq_list.objects.all()
    context = {'faqs':faqs}
    return render(request, 'base/faq.html', context)

def enquiry(request):
    mesg=''
    form = EnquiryForm()
    if request.method == 'POST':
        form=EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            mesg = 'Data has been saved.'
    
    form = EnquiryForm()
    context = {'form':form, 'mesg':mesg}
    return render(request, 'base/enquiry.html', context)

    
    context= {'form':form}
    return render(request, 'base/enquiry.html', context)

