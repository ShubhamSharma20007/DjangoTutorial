from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=102)
    emp_id = models.CharField(max_length=101)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=102)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=102)
    
    
class testimonial(models.Model):
    name = models.CharField(max_length=52)
    description = models.CharField(max_length=102)
    picture  = models.ImageField(upload_to="testimonial")
    rating = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    
    
