from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Banners)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Service, ServiceAdmin)

admin.site.register(models.Page)

admin.site.register(models.faq_list)

admin.site.register(models.Enquiry)

class GalleryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Gallery, GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(models.GalleryImage, GalleryImageAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_editable = ('highlight_status',)
    list_display=('title','price', 'highlight_status')
admin.site.register(models.Subscription, SubscriptionAdmin)

class SubscriptionFeatureAdmin(admin.ModelAdmin):
    list_display=('title', 'subscription')
admin.site.register(models.SubscriptionFeature, SubscriptionFeatureAdmin)