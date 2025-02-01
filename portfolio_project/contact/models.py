from django.db import models

# Create your models here.


class Contact(models.Model):
    choices=[
    ("Portfolio", "Portfolio"),
    ("E-Commerce", "E-Commerce"),
    ("Corporate", "Corporate"),
    ("Educational", "Educational"),
    ("Blog", "Blog"),
    ("News", "News"),
    ("Non-Profit", "Non-Profit"),
    ("Landing Page", "Landing Page"),
    ("Other", "Other"),
    
    ]
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=255,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    select_website=models.CharField(choices=choices,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    