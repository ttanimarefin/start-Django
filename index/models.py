from django.db import models

# Create your models here.
class aboutUs (models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=700,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)

    

    