from django.db import models

# Create your models here.
class Student( models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    upload = models.ImageField(upload_to ='uploads/' ,null=True) 
  
    
    def __str__(self):
        return self.name