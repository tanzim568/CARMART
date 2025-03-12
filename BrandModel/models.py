from django.db import models



# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='BrandModel/media/uploads')
    slug=models.SlugField(max_length=200,unique=True)
   
    def __str__(self):
        return f"Brand :{self.name}"