from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   

    path('pagedetail/<int:id>/', views.page_detail, name='pagedetail'),
    path('faq/', views.faq, name='faq'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallerydetail/<int:id>', views.gallery_detail, name='gallerydetail'),
    path('subscriptions/', views.subscription, name="subscription"),
    path('checkout/<int:sub_id>', views.checkout, name='checkout'),

    path('checkout_session/<int:sub_id>', views.checkout_session, name='checkout_session'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),





]