from django.db import models
from django.utils.safestring import mark_safe

from django.contrib.auth.models import User

# Create your models here


class Banners(models.Model):
    image = models.ImageField(upload_to='banners/')
    alt_text = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.alt_text}"
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100"/>' % (self.image.url))
                

class Service(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    image = models.ImageField(upload_to='services/', null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100"/>' % (self.image.url))
    

class Page(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.title
    
class faq_list(models.Model):
    question=models.CharField(max_length=200)
    answer=models.TextField()

    def __str__(self):
        return self.question
    

class Enquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    detail = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to='gallery/', null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100"/>' % (self.image.url))
    
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    alt_text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_image/', null=True)

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100"/>' % (self.image.url))
    

class Subscription(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    highlight_status = models.BooleanField(default=False)
    max_num = models.IntegerField(null=True)
    availiable = models.IntegerField(null=True)

    def __str__(self):
        return self.title
    
class SubscriptionFeature(models.Model):
    subscription = models.ManyToManyField(Subscription)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class discount(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=True)
    total_months = models.IntegerField()
    total_discount = models.IntegerField()

    def __str__(self):
        return str(self.total_months)


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField(upload_to='subs/')

    def __str__(self):
        return str(self.user)
    
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="100"/>' % (self.image.url))
        else:
            return 'no-image'

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_subscriber(sender, instance, created, **kwargs):
    if created:
        Subscriber.objects.create(user=instance)


class SubscribedUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=50)

class Trainer(models.Model):
    full_name =models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=False)
    detail = models.TextField()
    image = models.ImageField(upload_to='trainers/')

    def __str__(self):
        return str(self.full_name)
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100"/>' % (self.image.url))
    