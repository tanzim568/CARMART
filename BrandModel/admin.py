from django.contrib import admin
from django.db import models
from .import models


# Register your models here.
class BrandModelAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}
    list_display=['name','slug']
    
admin.site.register(models.Brand, BrandModelAdmin)