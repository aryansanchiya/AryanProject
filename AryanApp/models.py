from django.db import models

# Create your models here.
class Writing(models.Model):
    title = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    date = models.DateField()
    description = models.TextField()
    image1 = models.ImageField()
    link = models.URLField()
    description2 = models.TextField()
    Author = models.CharField(max_length=255)

class Services(models.Model):
    fullname = models.CharField(max_length=255);
    definition = models.TextField()
    company_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    

