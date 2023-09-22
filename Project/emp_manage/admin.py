from django.contrib import admin
from .models import Emp,testimonial



# customize admin panel 
class Customadmin(admin.ModelAdmin):
    list_display = ('name',"working","emp_id")
    search_fields = ['name']


# class customtesti(admin.ModelAdmin):
#     list_display = ("picture")        

# Register your models here.

admin.site.register(Emp,Customadmin)
admin.site.register(testimonial)