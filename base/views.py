from django.shortcuts import render
from .models import Banners, Service, Page, faq_list, Enquiry, Gallery, GalleryImage, Subscription, SubscriptionFeature
from .forms import EnquiryForm

from django.db.models import Count
from django.contrib.auth import authenticate


# Create your views here.

def home(request):
    banners = Banners.objects.all()
    services = Service.objects.all()[:3]
    gimages = GalleryImage.objects.all().order_by('-id')[:9]
    context = {'banners':banners, 'services':services, 'gimages':gimages}
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

    
    # context= {'form':form}
    # return render(request, 'base/enquiry.html', context)


def gallery(request):
    gallerys = Gallery.objects.all().order_by('-id')
    context = {'gallerys': gallerys}
    return render(request, 'base/gallery.html', context)

def gallery_detail(request, id):
    gallery = Gallery.objects.get(id=id)
    gallery_img = GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    context = {'gallery_img':gallery_img, 'gallery':gallery}
    return render(request, 'base/detailgallery.html', context)

def subscription(request):
    subscription = Subscription.objects.all().order_by('price')
    distinct_features = SubscriptionFeature.objects.all()
    context = {'subscription':subscription, 'distinct_features': distinct_features}
    return render(request, 'base/pricing.html', context)


def checkout(request, sub_id):
    SubscriptionDetail = Subscription.objects.get(pk=sub_id)
    sub_feature = SubscriptionFeature.objects.all()
    context = {'subscriptiondetail': SubscriptionDetail, 'sub_feature': sub_feature}
    return render(request, 'base/checkout.html', context)




