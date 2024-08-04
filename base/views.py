from django.shortcuts import render, redirect
from .models import *
from .forms import EnquiryForm

from django.db.models import Count
from django.contrib.auth import authenticate

import stripe




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
    discounts = discount.objects.all()
    context = {'subscriptiondetail': SubscriptionDetail, 'sub_feature': sub_feature, 'discounts':discounts}
    return render(request, 'base/checkout.html', context)


stripe.api_key = 'sk_test_51Pk1arGyHjcugVxzLz0xVbHBNHyM9yNcw144jJ8uUGOw4oqoMj5X0uXQfQbQJRuszF5UniW9QEVnHgP1l8l6jvJR00xbIfDtuP'
def checkout_session(request, sub_id ):
    plan = Subscription.objects.get(pk=sub_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'npr',
                'product_data': {
                    'name': plan.title,
                },
                'unit_amount': plan.price*100,
            },
            'quantity':1,
        }],
        mode='payment',
        success_url = 'http://127.0.0.1:8000/payment_success',
        cancel_url='http://127.0.0.1:8000/payment_cancel',
    )
    return redirect(session.url, code=303)

def payment_success(request):
    return render(request, 'base/success.html')

def payment_cancel(request):
    return render(request, 'base/cancel.html')