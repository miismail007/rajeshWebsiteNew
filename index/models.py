from unicodedata import category
from django.db import models
from datetime import date
import datetime
from datetime import datetime

# Create your models here.

class blognew(models.Model):
    
    title=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=5000,blank=True,null=True)
    image=models.ImageField(upload_to='blognew/',blank=True,null=True)
    date123 = models.DateField(default=datetime.now)
    # link=models.CharField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=100,blank=True,null=True)
    
    

    def __str__(self):
        return self.title
    


class contactform(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.CharField(max_length=100,blank=False)
    
    message=models.TextField(max_length=800,blank=False)
    

    def __str__(self):
        return self.name


class portfolio_photos(models.Model):
    projectname=models.CharField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(upload_to='portfolio_photos/',blank=True,null=True)

    def __str__(self):
        return self.projectname



class about(models.Model):
   
    
    description=models.TextField(max_length=10000,blank=False)
    

    def __str__(self):
        return self.description



class experience(models.Model):
    role=models.CharField(max_length=100,blank=False)
    years=models.CharField(max_length=100,blank=False)
    
    description=models.TextField(max_length=1000,blank=False)
    

    def __str__(self):
        return self.role



class education(models.Model):
    role=models.CharField(max_length=100,blank=False)
    years=models.CharField(max_length=100,blank=False)
    
    description=models.TextField(max_length=1000,blank=False)
    

    def __str__(self):
        return self.role