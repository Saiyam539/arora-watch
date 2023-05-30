from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=20)
    availability = models.BooleanField(default=True)
    brand_photo = models.ImageField(upload_to='brand-img',default='')
    def __str__(self):
        return self.brand_name;
    
class Brand_watch(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='watch')
    watch_name = models.CharField(max_length=20)
    watch_photo = models.ImageField(upload_to='watch-img',default='')
    watch_price = models.CharField(max_length=30,default='0')
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.brand.brand_name+"--"+self.watch_name;


