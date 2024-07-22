from django.db import models
from django.utils.safestring import mark_safe

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