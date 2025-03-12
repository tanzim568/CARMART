from django.db import models
from BrandModel.models import Brand


# Create your models here.

class Car(models.Model): #beshi r modde kom foreignkey
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='CarModel/media/uploads')
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand',null=True,blank=True)

    def __str__(self):
        return self.name
    