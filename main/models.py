from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')



class Contact(models.Model):
    name = models.CharField(max_length=90,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField(max_length=90,null=True, blank=True)
    age = models.IntegerField(null=True,blank=True)
    message = models.TextField(max_length=1000,null=True,blank=True)
    sex = models.CharField(max_length=100,null=True,blank=True)
